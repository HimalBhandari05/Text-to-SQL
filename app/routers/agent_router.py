import time
from fastapi import APIRouter
from pydantic import BaseModel
from logger import get_logger
from services.decomposer import decompose_question
from services.sql_generator import generate_sql
from services.retry_engine import run_with_retry
from services.summarizer import summarize_result

logger = get_logger(__name__)
router = APIRouter()


class AgentRequest(BaseModel):
    question: str


def _extract_result(rows: list):
    """Return scalar value for single-cell results, full list otherwise."""
    if rows and len(rows) == 1 and len(rows[0]) == 1:
        return list(rows[0].values())[0]
    return rows


@router.post("/agent/sql")
def agent_sql(request: AgentRequest):
    start = time.time()
    question = request.question
    logger.info(f"[Agent] ── New request ──────────────────────────")
    logger.info(f"[Agent] Question: {question}")

    # ── Step 1: Decompose ──────────────────────────────────────────────────
    try:
        decomposition = decompose_question(question)
        logger.info(f"[Agent] Step 1 ✓ Decomposition complete")
    except Exception as e:
        logger.warning(f"[Agent] Step 1 ✗ Decomposition failed ({e}), continuing without it")
        decomposition = None

    # ── Step 2: Generate SQL ───────────────────────────────────────────────
    try:
        sql = generate_sql(question, decomposition)
        logger.info(f"[Agent] Step 2 ✓ SQL: {sql}")
    except ValueError as e:
        elapsed = round((time.time() - start) * 1000, 2)
        logger.error(f"[Agent] Step 2 ✗ Blocked in {elapsed}ms: {e}")
        return {
            "sql": None,
            "result": None,
            "summary": "I was unable to answer your question because it requires a non-SELECT operation.",
            "status": "blocked",
            "retries": 0,
        }
    except Exception as e:
        elapsed = round((time.time() - start) * 1000, 2)
        logger.error(f"[Agent] Step 2 ✗ Generation failed in {elapsed}ms: {type(e).__name__}: {e}")
        return {
            "sql": None,
            "result": None,
            "summary": "I was unable to answer your question due to a SQL generation error. Please try rephrasing.",
            "status": "failed",
            "retries": 0,
            "error": f"{type(e).__name__}: {e}",
        }

    # ── Steps 3 & 4: Execute with up to 3 retries ─────────────────────────
    result = run_with_retry(question, sql, max_retries=3)
    elapsed = round((time.time() - start) * 1000, 2)

    logger.info(
        f"[Agent] Steps 3-4 ✓ status={result['status']} | "
        f"retries={result['retries']} | elapsed={elapsed}ms"
    )

    if result["status"] != "success":
        logger.error(f"[Agent] All retries exhausted after {elapsed}ms")
        return {
            "sql": result["sql"],
            "result": None,
            "summary": "I was unable to answer your question due to a database error. Please try rephrasing.",
            "status": "failed",
            "retries": result["retries"],
        }

    # ── Step 5: Summarize ──────────────────────────────────────────────────
    try:
        summary = summarize_result(question, result["sql"], result["rows"])
        logger.info(f"[Agent] Step 5 ✓ Summary generated")
    except Exception as e:
        logger.warning(f"[Agent] Step 5 ✗ Summarizer failed ({e}), using fallback")
        summary = f"The query returned {result['row_count']} result(s)."

    logger.info(f"[Agent] ── Request complete in {elapsed}ms ──────")

    return {
        "sql": result["sql"],
        "result": _extract_result(result["rows"]),
        "summary": summary,
        "status": "success",
        "retries": result["retries"],
    }
