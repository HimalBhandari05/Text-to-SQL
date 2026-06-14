# API Documentation

The Text-to-SQL system provides two primary interfaces to interact with the database using natural language: a **Direct Pipeline** endpoint and a fully **Agentic** endpoint.

Interactive Swagger API docs can be viewed locally at:
👉 **[http://127.0.0.1:8001/docs](http://127.0.0.1:8001/docs)**

---

## 1. Root Endpoint

Check service availability and discover available endpoints.

- **Method**: `GET`
- **Path**: `/`
- **Headers**: None
- **Response Format**: `application/json`

### Example Response
```json
{
  "message": "Text-to-SQL API is running",
  "endpoints": {
    "task3": "POST /pipeline/query",
    "task4": "POST /agent/sql"
  }
}
```

---

## 2. Direct Pipeline Endpoint

Runs a simpler version of the pipeline. It skips the query decomposition stage and runs a maximum of **1 retry** on failure. Recommended for simpler questions that do not require complex query breakdown.

- **Method**: `POST`
- **Path**: `/pipeline/query`
- **Headers**:
  - `Content-Type: application/json`
- **Request Body**:
  ```json
  {
    "question": "string"
  }
  ```

### Response Formats

#### Successful Execution
```json
{
  "question": "How many employees work at the company?",
  "sql": "SELECT COUNT(*) AS employee_count FROM employees",
  "status": "success",
  "row_count": 1,
  "result": [
    {
      "employee_count": 23
    }
  ],
  "retried": false
}
```

#### Blocked Query (Security Breach)
If a user attempts SQL injection or queries non-SELECT statements:
```json
{
  "question": "DROP TABLE customers;",
  "sql": null,
  "status": "blocked",
  "row_count": 0,
  "result": [],
  "retried": false,
  "error": "Query blocked: contains 'DROP'. Only SELECT queries are allowed."
}
```

---

## 3. Agentic SQL Endpoint

Runs the complete 5-stage agentic workflow: Query Decomposition ➔ SQL Generation ➔ Validation ➔ Database Execution (with up to **3 retries** on failure) ➔ Natural Language Summarization.

- **Method**: `POST`
- **Path**: `/agent/sql`
- **Headers**:
  - `Content-Type: application/json`
- **Request Body**:
  ```json
  {
    "question": "string"
  }
  ```

### Response Formats

#### Successful Execution (Returning List)
```json
{
  "sql": "SELECT \"city\", \"phone\" FROM offices WHERE \"country\" = 'USA'",
  "result": [
    {
      "city": "San Francisco",
      "phone": "+1 650 219 4782"
    },
    {
      "city": "Boston",
      "phone": "+1 215 837 0825"
    },
    {
      "city": "NYC",
      "phone": "+1 212 555 3000"
    }
  ],
  "summary": "The offices in the USA are located in San Francisco (+1 650 219 4782), Boston (+1 215 837 0825), and NYC (+1 212 555 3000).",
  "status": "success",
  "retries": 0
}
```

#### Successful Execution (Returning Scalar Celled Result)
If a query results in a single column and a single row (like a count or sum), the response unwraps the result into a scalar type:
```json
{
  "sql": "SELECT COUNT(*) FROM products",
  "result": 110,
  "summary": "There are a total of 110 products in the database.",
  "status": "success",
  "retries": 0
}
```

#### Blocked Query (Non-SELECT or Blocked Keyword)
```json
{
  "sql": null,
  "result": null,
  "summary": "I was unable to answer your question because it requires a non-SELECT operation.",
  "status": "blocked",
  "retries": 0
}
```

#### Failed Query (Error during generation or database execution)
```json
{
  "sql": "SELECT invalid_column FROM employees",
  "result": null,
  "summary": "I was unable to answer your question due to a database error. Please try rephrasing.",
  "status": "failed",
  "retries": 3
}
```
