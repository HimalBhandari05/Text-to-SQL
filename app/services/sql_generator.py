import os
import time
from google import genai
from dotenv import load_dotenv
from logger import get_logger
from services.validator import validate_and_clean

load_dotenv()
logger = get_logger(__name__)

MODEL = "gemini-2.5-flash"
PROMPT_PATH = os.path.join(os.path.dirname(__file__), "..", "prompts", "sql_generation_prompt.txt")

_client = None

# Transient HTTP status codes worth retrying
_RETRYABLE = ("503", "UNAVAILABLE", "429", "RESOURCE_EXHAUSTED")


def _get_client() -> genai.Client:
    global _client
    if _client is None:
        _client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
    return _client


def _load_prompt() -> str:
    with open(PROMPT_PATH, "r") as f:
        return f.read()


def _is_retryable(exc: Exception) -> bool:
    err = str(exc)
    return any(code in err for code in _RETRYABLE)


def generate_sql(question: str, decomposition: dict = None) -> str:
    template = _load_prompt()

    # BUG FIX: build the full question string first, THEN do a single replace.
    # The old code replaced {question} twice — the second replace was always a no-op
    # because {question} was already gone after the first replace.
    if decomposition:
        context_block = (
            f"\n## Structured Analysis\n"
            f"Intent: {decomposition.get('intent', '')}\n"
            f"Tables: {', '.join(decomposition.get('tables', []))}\n"
            f"Columns: {', '.join(decomposition.get('columns', []))}\n"
            f"Filters: {decomposition.get('filters', 'None')}\n"
            f"Joins: {decomposition.get('joins', 'None')}\n"
        )
        full_question = question + "\n" + context_block
    else:
        full_question = question

    prompt = template.replace("{question}", full_question)

    logger.info(f"[SQL Generator] Generating SQL for: {question}")

    last_exc: Exception | None = None
    for attempt in range(1, 4):  # up to 3 attempts for transient API errors
        try:
            response = _get_client().models.generate_content(model=MODEL, contents=prompt)

            # BUG FIX: response.text is None when the model returns only thinking tokens
            # or when the response is blocked by safety filters. Calling .strip() on None
            # raises AttributeError which was silently swallowed by the router.
            raw = response.text
            if raw is None:
                finish = (
                    response.candidates[0].finish_reason
                    if response.candidates else "unknown"
                )
                logger.error(
                    f"[SQL Generator] response.text is None — "
                    f"finish_reason={finish} | candidates={response.candidates}"
                )
                raise ValueError(
                    f"Gemini returned an empty response (text=None, finish_reason={finish}). "
                    "The model may have been blocked by safety filters."
                )

            raw = raw.strip()
            logger.info(f"[SQL Generator] Raw response: {raw}")

            sql = validate_and_clean(raw)
            logger.info(f"[SQL Generator] Validated SQL: {sql}")
            return sql

        except ValueError:
            raise  # validation / blocked-keyword errors — don't retry

        except Exception as exc:
            last_exc = exc
            if _is_retryable(exc):
                wait = 2 ** attempt  # 2 s, 4 s, 8 s
                logger.warning(
                    f"[SQL Generator] Attempt {attempt}/3 — transient error "
                    f"({type(exc).__name__}: {exc}). Retrying in {wait}s…"
                )
                time.sleep(wait)
            else:
                logger.error(
                    f"[SQL Generator] Attempt {attempt}/3 — non-retryable error: "
                    f"{type(exc).__name__}: {exc}"
                )
                raise

    logger.error(
        f"[SQL Generator] All 3 attempts failed. "
        f"Last error: {type(last_exc).__name__}: {last_exc}"
    )
    raise last_exc
