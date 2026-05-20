import re
from logger import get_logger

logger = get_logger(__name__)

BLOCKED_KEYWORDS = {
    "DELETE", "DROP", "UPDATE", "INSERT",
    "TRUNCATE", "ALTER", "CREATE", "REPLACE",
}


def validate_and_clean(sql: str) -> str:
    # Strip markdown code fences Claude sometimes wraps output in
    sql = re.sub(r"```sql\s*", "", sql, flags=re.IGNORECASE)
    sql = re.sub(r"```\s*", "", sql)
    sql = sql.strip()

    upper = sql.upper()

    for keyword in BLOCKED_KEYWORDS:
        if re.search(rf"\b{keyword}\b", upper):
            logger.warning(f"[Validator] Blocked keyword detected: {keyword}")
            raise ValueError(
                f"Query blocked: contains '{keyword}'. Only SELECT queries are allowed."
            )

    if not upper.lstrip().startswith("SELECT"):
        raise ValueError("Query blocked: query must start with SELECT.")

    return sql
