# Setup Guide

This guide walks you through setting up the Text-to-SQL application from scratch.

## Prerequisites

Before starting, ensure you have the following installed on your system:
- **Python 3.12+** (managed easily via `uv`)
- **Docker & Docker Compose** (for running the PostgreSQL database)
- **uv** (Modern, ultra-fast Python package and project manager)
  - Install `uv` via:
    ```bash
    # macOS/Linux
    curl -LsSf https://astral.sh/uv/install.sh | sh
    
    # Windows (PowerShell)
    powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```

---

## Step-by-Step Installation

### 1. Clone the Repository
Clone the repository and navigate into the project root directory:
```bash
git clone <repository-url>
cd Text-to-SQL
```

### 2. Install Dependencies
Sync project dependencies using `uv`. This automatically creates a virtual environment (`.venv`) and installs the exact versions locked in `uv.lock`:
```bash
uv sync
```

### 3. Environment Variables Setup
Copy the sample environment file to create your local `.env`:
```bash
cp .env.example .env
```

Open the newly created `.env` file and insert your Google Gemini API key:
```env
GOOGLE_API_KEY=your_actual_gemini_api_key
```
> [!NOTE]
> You can obtain an API key from the [Google AI Studio](https://aistudio.google.com/).

### 4. Database Setup (Docker)
Start the PostgreSQL container in detached mode. This service pulls the lightweight PostgreSQL 16 Alpine image and seeds it with the `ClassicModels` dataset:
```bash
docker compose up -d
```

#### Verifying Database Health
You can check if the container is running by running:
```bash
docker ps
```
Look for a container named `postgres_database` running on host port `5400`.

### 5. Running the Application
Start the FastAPI development server:
```bash
uv run uvicorn app.main:app --reload --port 8001
```

Once running, you can access the Interactive API Documentation (Swagger UI) at:
👉 **[http://127.0.0.1:8001/docs](http://127.0.0.1:8001/docs)**

---

## Verifying Setup (Optional Helper Script)

To quickly verify that your database connection is active, and your Gemini API key works, run the included verify script:
```bash
uv run scripts/verify_setup.py
```
*(If the script is not present, see the repository enhancements section to install it.)*
