import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI
from pydantic import BaseModel
from logger import get_logger
from services.sql_generator import generate_sql
from services.retry_engine import run_with_retry
from routers.agent_router import router as agent_router

logger = get_logger(__name__)

app = FastAPI(
    title="Text-to-SQL System",
    version="2.0.0",
    description="Task 3: POST /pipeline/query | Task 4: POST /agent/sql",
)

app.include_router(agent_router)


# ── Task 3: Direct pipeline endpoint ──────────────────────────────────────────

class QueryRequest(BaseModel):
    question: str


@app.post("/pipeline/query")
def pipeline_query(request: QueryRequest):
    logger.info(f"[Pipeline] Question: {request.question}")

    try:
        sql = generate_sql(request.question)
    except ValueError as e:
        logger.error(f"[Pipeline] Blocked: {e}")
        return {
            "question": request.question,
            "sql": None,
            "status": "blocked",
            "row_count": 0,
            "result": [],
            "retried": False,
            "error": str(e),
        }
    except Exception as e:
        logger.error(f"[Pipeline] Generation failed: {type(e).__name__}: {e}")
        return {
            "question": request.question,
            "sql": None,
            "status": "failed",
            "row_count": 0,
            "result": [],
            "retried": False,
            "error": f"{type(e).__name__}: {e}",
        }

    result = run_with_retry(request.question, sql, max_retries=1)

    response = {
        "question": request.question,
        "sql": result["sql"],
        "status": result["status"],
        "row_count": result["row_count"],
        "result": result["rows"],
        "retried": result["retried"],
    }

    if result["status"] != "success":
        response["error"] = result["error"]

    logger.info(f"[Pipeline] Complete — status: {result['status']}")
    return response


@app.get("/")
def root():
    return {
        "message": "Text-to-SQL API is running",
        "endpoints": {
            "task3": "POST /pipeline/query",
            "task4": "POST /agent/sql",
        },
    }
