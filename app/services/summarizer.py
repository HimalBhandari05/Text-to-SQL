import os
import json
from google import genai
from dotenv import load_dotenv
from logger import get_logger

load_dotenv()
logger = get_logger(__name__)

MODEL = "gemini-2.5-flash"
PROMPT_PATH = os.path.join(os.path.dirname(__file__), "..", "prompts", "summary_prompt.txt")

_client = None


def _get_client() -> genai.Client:
    global _client
    if _client is None:
        _client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
    return _client


def _load_prompt() -> str:
    with open(PROMPT_PATH, "r") as f:
        return f.read()


def summarize_result(question: str, sql: str, rows: list) -> str:
    sample = rows[:10] if len(rows) > 10 else rows

    prompt = (
        _load_prompt()
        .replace("{question}", question)
        .replace("{sql}", sql)
        .replace("{result}", json.dumps(sample, default=str))
    )

    logger.info("[Summarizer] Generating natural language summary")

    summary = _get_client().models.generate_content(model=MODEL, contents=prompt).text.strip()
    logger.info(f"[Summarizer] {summary}")

    return summary
