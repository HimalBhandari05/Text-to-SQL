# Agentic Text-to-SQL System 🚀

An agentic, multi-stage Text-to-SQL translation, execution, self-correction, and summarization pipeline built using FastAPI, PostgreSQL, SQLAlchemy, and the Google Gemini API.

This project is structured for enterprise-grade reproducibility, security, and developer onboarding.

---

## 📖 Table of Contents
1. [Project Overview](#-project-overview)
2. [Features](#-features)
3. [Tech Stack](#-tech-stack)
4. [Architecture Overview](#-architecture-overview)
5. [Project Structure](#-project-structure)
6. [Installation & Setup](#-installation--setup)
7. [API Documentation](#-api-documentation)
8. [Troubleshooting](#-troubleshooting)
9. [GitHub Quality Improvements](#-github-quality-improvements)
10. [Future Improvements](#-future-improvements)

---

## 🌟 Project Overview

This system allows developers, assessors, and end-users to query a relational database (`ClassicModels` store schema) using plain natural language questions (e.g., *"Show me all offices in the USA and their phone numbers"* or *"What is our total revenue this quarter?"*). 

The application utilizes the **Google Gemini API** (`gemini-2.5-flash`) to decompose the query, generate the SQL, and summarize the results. Crucially, it integrates a **self-correcting retry loop** that fixes broken SQL queries on-the-fly and applies **strict validation rules** to prevent destructive SQL operations.

---

## 🛠 Features

- **Query Decomposition**: Breaks down complex user requests into structured intents (tables, columns, joins, filters) before SQL generation.
- **SQL Generation**: Generates compliant PostgreSQL queries based on schema context.
- **SQL Validation**: Protects against SQL injection and data-modifying queries (allows only read-only `SELECT` statements).
- **Execution & Telemetry**: Runs queries against a Dockerized PostgreSQL instance and logs performance timings.
- **Self-Healing Retry Engine**: Captures database exceptions (syntax errors, casing problems) and re-queries the LLM with error context to auto-fix the query.
- **Natural Language Summarization**: Translates raw database rows back into friendly conversational responses.
- **Agentic SQL Endpoint**: A fully-managed endpoint exposing the entire multi-stage workflow.

---

## 💻 Tech Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/) (Async web API)
- **Database Engine**: [PostgreSQL 16](https://www.postgresql.org/) (Dockerized container)
- **ORM / Connector**: [SQLAlchemy 2.0](https://www.sqlalchemy.org/) & `psycopg2-binary`
- **LLM Provider**: [Google Gemini API](https://aistudio.google.com/) (`google-genai` SDK)
- **Dependency Manager**: [uv](https://github.com/astral-sh/uv) (Extremely fast Python packager)
- **Language**: Python 3.12

---

## 🏗 Architecture Overview

The pipeline executes user questions in a structured loop. The flow of data is as follows:

```
User Question
      ↓
Query Decomposer (Extracts structural schema hints)
      ↓
SQL Generator (Synthesizes ANSI SQL query)
      ↓
SQL Validator (Enforces security and read-only constraints)
      ↓
SQL Executor (Queries PostgreSQL, catches driver exceptions)
      ↓
Retry Engine (Loops error message back to LLM to self-heal SQL)
      ↓
NL Summarizer (Formats query rows into natural language sentences)
      ↓
Response to User
```

For a detailed explanation of each architectural phase, see the [Architecture Documentation](file:///home/himalbhandari/Text-to-SQL/docs/architecture.md).

---

## 📁 Project Structure

Below is the directory structure highlighting key files and their purposes:

```
Text-to-SQL/
├── app/
│   ├── main.py                 # FastAPI Application Server Entrypoint
│   ├── database.py             # Database Engine & SQLAlchemy Session setup
│   ├── logger.py               # Shared Structured Logging Configuration
│   ├── routers/
│   │   └── agent_router.py     # Agentic Endpoint router (/agent/sql)
│   ├── services/
│   │   ├── decomposer.py       # LLM Question Decomposition
│   │   ├── sql_generator.py    # LLM SQL Generator
│   │   ├── validator.py        # SQL Security/Constraint Validator
│   │   ├── executor.py         # DB Query execution logic
│   │   ├── retry_engine.py     # Self-healing retry and error parser
│   │   └── summarizer.py       # LLM NL Summarizer
│   └── prompts/
│       ├── decomposition_prompt.txt
│       ├── sql_generation_prompt.txt
│       ├── retry_prompt.txt
│       └── summary_prompt.txt
├── docs/                       # Comprehensive System Documentation
│   ├── setup.md                # Local setup guide
│   ├── architecture.md         # Extended architecture and component flow
│   ├── api.md                  # API payload formats & examples
│   └── troubleshooting.md      # Common failure cases & recovery actions
├── scripts/
│   └── verify_setup.py         # Automated health checking script
├── docker-compose.yml          # Container configuration for PostgreSQL
├── seed.sql                    # SQL dump containing ClassicModels schema and data
├── pyproject.toml              # Dependencies declaration
├── uv.lock                     # Locked dependency manifest
├── .env.example                # Sample environment configuration file
└── README.md                   # This file
```

- **Server Entrypoint**: [app/main.py](file:///home/himalbhandari/Text-to-SQL/app/main.py)
- **Database Engine**: [app/database.py](file:///home/himalbhandari/Text-to-SQL/app/database.py)
- **Agent Router**: [app/routers/agent_router.py](file:///home/himalbhandari/Text-to-SQL/app/routers/agent_router.py)
- **Retry Engine**: [app/services/retry_engine.py](file:///home/himalbhandari/Text-to-SQL/app/services/retry_engine.py)

---

## ⚙️ Installation & Setup

Get the environment running in under 2 minutes:

```bash
# 1. Clone the repository
git clone <repo-url>
cd Text-to-SQL

# 2. Sync virtualenv & dependencies with uv
uv sync

# 3. Create environment file
cp .env.example .env
# Edit .env and supply your GOOGLE_API_KEY

# 4. Start the database container
docker compose up -d

# 5. Launch the API server
uv run uvicorn app.main:app --reload --port 8001
```

Access Swagger UI docs at: **[http://127.0.0.1:8001/docs](http://127.0.0.1:8001/docs)**

For extended setup configurations, database volume management, and detailed steps, check the [Setup Guide](file:///home/himalbhandari/Text-to-SQL/docs/setup.md).

---

## 🔌 API Documentation

### POST `/agent/sql` (Agentic Route)
Runs the full pipeline, decomposes the question, executes it, self-heals up to 3 times, and summarizes the outcome.

**Request Body**:
```json
{
  "question": "Show the cities and phone numbers of offices in France"
}
```

**Response Body**:
```json
{
  "sql": "SELECT \"city\", \"phone\" FROM offices WHERE \"country\" = 'France'",
  "result": [
    {
      "city": "Paris",
      "phone": "+33 14 723 4404"
    }
  ],
  "summary": "We have one office in France, located in Paris. The telephone contact is +33 14 723 4404.",
  "status": "success",
  "retries": 0
}
```

### POST `/pipeline/query` (Direct Route)
A simpler endpoint that generates and executes SQL directly (with at most 1 retry and no summarizer).

Refer to the [API Documentation](file:///home/himalbhandari/Text-to-SQL/docs/api.md) for full request/response schemas, failure formats, and scalar output examples.

---

## 🚨 Troubleshooting

If you run into setup issues, refer to the [Troubleshooting Documentation](file:///home/himalbhandari/Text-to-SQL/docs/troubleshooting.md) for solutions to:
- **Invalid Gemini API Key** (HTTP `400` / `ResourceExhausted`)
- **PostgreSQL Authentication Failed**
- **Docker Container Not Running**
- **Port 5400 Already in Use**
- **Gemini Service Unavailable** (HTTP `503`)

---

## 🛡️ GitHub Quality Improvements

To prepare this repository for public distribution, the following enhancements have been introduced:
1. **Clean Code Isolation**: Separation of business logic (in [app/services/](file:///home/himalbhandari/Text-to-SQL/app/services/)) from routing (in [app/routers/](file:///home/himalbhandari/Text-to-SQL/app/routers/)) and entrypoints (in [app/main.py](file:///home/himalbhandari/Text-to-SQL/app/main.py)).
2. **Robust Transient Exception Handling**: Implemented exponential backoff sleep-retries (2s, 4s, 8s) in LLM-facing components ([app/services/sql_generator.py](file:///home/himalbhandari/Text-to-SQL/app/services/sql_generator.py) and [app/services/decomposer.py](file:///home/himalbhandari/Text-to-SQL/app/services/decomposer.py)) to handle Google Gemini API rate limits (`429`) and temporary backend outages (`503`).
3. **Pydantic Validation**: Fully typed request schemas prevent malformed API calls.
4. **Environment Isolation**: Prevented hardcoded secrets by referencing environment variables loaded via `python-dotenv`.
5. **Database Port Decoupling**: Configured host port `5400` mapping to avoid conflicts with native PostgreSQL installs running on default `5432`.
6. **Logging Telemetry**: Replaced print statements with standard log levels (INFO, WARNING, ERROR) outputting to both console and [logs/app.log](file:///home/himalbhandari/Text-to-SQL/logs/app.log) files for auditing.
7. **Security Guardrails**: Added a SQL syntax verification mechanism in [app/services/validator.py](file:///home/himalbhandari/Text-to-SQL/app/services/validator.py) which restricts user input from executing data manipulation commands (`DROP`, `DELETE`, `UPDATE`, `INSERT`).

---

## 📈 Future Improvements

- **Semantic Query Caching**: Store question-to-SQL maps in Redis to avoid hitting the LLM for identical natural language queries.
- **Dynamic Few-Shot Prompting**: Maintain an index of question-SQL pairs in a vector database (e.g. ChromaDB/pgvector) and dynamically inject the top-K matching schema examples into the prompt.
- **Multi-Database Support**: Extend the ORM adapter to toggle between PostgreSQL, SQLite, MySQL, and Snowflake.
- **Fine-Tuned LLM Models**: Train a smaller, open-source model (e.g. Llama-3-code / Codegen) specifically on the company's database schemas for reduced latency and offline capabilities.
- **Web UI Dashboard**: Build a React or Next.js user interface with interactive charts that maps SQL query results into graphs (bar charts, line graphs) automatically.
