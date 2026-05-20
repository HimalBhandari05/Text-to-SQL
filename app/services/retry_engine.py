import os
from google import genai
from dotenv import load_dotenv
from logger import get_logger
from services.validator import validate_and_clean
from services.executor import execute_query

load_dotenv()
logger = get_logger(__name__)

MODEL = "gemini-2.5-flash"
PROMPT_PATH = os.path.join(os.path.dirname(__file__), "..", "prompts", "retry_prompt.txt")

_client = None


def _get_client() -> genai.Client:
    global _client
    if _client is None:
        _client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
    return _client


def _load_prompt() -> str:
    with open(PROMPT_PATH, "r") as f:
        return f.read()


def run_with_retry(question: str, sql: str, max_retries: int = 1) -> dict:
    result = execute_query(sql)
    retry_count = 0

    if result["status"] == "success":
        return {**result, "retried": False, "retries": 0}

    template = _load_prompt()

    for attempt in range(1, max_retries + 1):
        retry_count = attempt
        logger.warning(f"[Retry] Attempt {attempt}/{max_retries} — Error: {result['error']}")

        prompt = (
            template
            .replace("{question}", question)
            .replace("{sql}", sql)
            .replace("{error}", result["error"] or "Unknown error")
        )

        raw = _get_client().models.generate_content(model=MODEL, contents=prompt).text.strip()

        try:
            fixed_sql = validate_and_clean(raw)
            logger.info(f"[Retry] Attempt {attempt} — Fixed SQL: {fixed_sql}")
        except ValueError as e:
            logger.error(f"[Retry] Attempt {attempt} — Validation failed: {e}")
            continue

        sql = fixed_sql
        result = execute_query(sql)

        if result["status"] == "success":
            logger.info(f"[Retry] Attempt {attempt} succeeded")
            return {**result, "retried": True, "retries": retry_count}

        logger.error(f"[Retry] Attempt {attempt} still failed: {result['error']}")

    logger.error(f"[Retry] All {max_retries} attempt(s) exhausted")
    return {**result, "retried": True, "retries": retry_count}
