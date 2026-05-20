import os
import re
import json
import time
from google import genai
from dotenv import load_dotenv
from logger import get_logger

load_dotenv()
logger = get_logger(__name__)

MODEL = "gemini-2.5-flash"
PROMPT_PATH = os.path.join(os.path.dirname(__file__), "..", "prompts", "decomposition_prompt.txt")

_client = None

_RETRYABLE = ("503", "UNAVAILABLE", "429", "RESOURCE_EXHAUSTED")


def _get_client() -> genai.Client:
    global _client
    if _client is None:
        _client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
    return _client


def _load_prompt() -> str:
    with open(PROMPT_PATH, "r") as f:
        return f.read()


def decompose_question(question: str) -> dict:
    prompt = _load_prompt().replace("{question}", question)
    logger.info(f"[Decomposer] Decomposing: {question}")

    last_exc: Exception | None = None
    for attempt in range(1, 4):
        try:
            response = _get_client().models.generate_content(model=MODEL, contents=prompt)

            raw = response.text
            if raw is None:
                finish = (
                    response.candidates[0].finish_reason
                    if response.candidates else "unknown"
                )
                raise ValueError(f"Gemini returned empty response (text=None, finish_reason={finish})")

            raw = raw.strip()

            # Strip markdown fences if Gemini wraps the JSON
            raw = re.sub(r"```json\s*", "", raw, flags=re.IGNORECASE)
            raw = re.sub(r"```\s*", "", raw).strip()

            decomposition = json.loads(raw)
            logger.info(
                f"[Decomposer] Intent: {decomposition.get('intent')} | "
                f"Tables: {decomposition.get('tables')} | "
                f"Filters: {decomposition.get('filters')}"
            )
            return decomposition

        except Exception as exc:
            last_exc = exc
            err = str(exc)
            if any(code in err for code in _RETRYABLE):
                wait = 2 ** attempt
                logger.warning(
                    f"[Decomposer] Attempt {attempt}/3 — transient error "
                    f"({type(exc).__name__}: {exc}). Retrying in {wait}s…"
                )
                time.sleep(wait)
            else:
                logger.error(f"[Decomposer] Attempt {attempt}/3 — non-retryable: {type(exc).__name__}: {exc}")
                raise

    logger.error(f"[Decomposer] All 3 attempts failed. Last: {type(last_exc).__name__}: {last_exc}")
    raise last_exc
