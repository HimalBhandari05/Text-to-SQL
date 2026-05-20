import time
from sqlalchemy import text
from database import engine
from logger import get_logger

logger = get_logger(__name__)


def execute_query(sql: str) -> dict:
    start = time.time()
    logger.info(f"[Executor] Running query: {sql}")

    try:
        with engine.connect() as conn:
            result = conn.execute(text(sql))
            rows = [dict(row._mapping) for row in result]
            elapsed = round((time.time() - start) * 1000, 2)

            logger.info(f"[Executor] Success — {len(rows)} rows returned in {elapsed}ms")

            return {
                "status": "success",
                "sql": sql,
                "rows": rows,
                "row_count": len(rows),
                "error": None,
                "elapsed_ms": elapsed,
            }

    except Exception as e:
        elapsed = round((time.time() - start) * 1000, 2)
        logger.error(f"[Executor] Failed in {elapsed}ms — {str(e)}")

        return {
            "status": "error",
            "sql": sql,
            "rows": [],
            "row_count": 0,
            "error": str(e),
            "elapsed_ms": elapsed,
        }
