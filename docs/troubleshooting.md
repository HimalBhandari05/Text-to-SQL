# Troubleshooting Guide

This guide describes common errors that may occur when setting up or running the Text-to-SQL system, along with step-by-step diagnostic actions to resolve them.

---

## 1. Invalid Gemini API Key

### Symptoms
- In the application logs, you see API exceptions with error codes like `400` or `APIKeyServiceClient` errors.
- Text-to-SQL generation fails immediately with messages containing `API key not valid` or `Invalid API key`.

### Diagnosis & Resolution
1. Verify that you have created a `.env` file from `.env.example` in the project root:
   ```bash
   ls -a
   ```
2. Verify that `GOOGLE_API_KEY` is present and does not contain placeholders (e.g., `your_api_key_here`).
3. Check if the API key is active. Go to the [Google AI Studio](https://aistudio.google.com/) and create a new key if necessary.
4. If you have exported it manually in your shell session, make sure it is exported properly:
   ```bash
   echo $GOOGLE_API_KEY
   ```

---

## 2. PostgreSQL Authentication Failed

### Symptoms
- In the application logs: `sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) connection to server at "localhost" (127.0.0.1), port 5400 failed: FATAL: password authentication failed for user "postgres"`.

### Diagnosis & Resolution
1. Check that the database credentials in `.env` match those set in the Docker container.
2. In your `.env`, check:
   ```env
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=postgres
   POSTGRES_DB=classicmodels
   ```
3. If you changed the password in `.env` *after* running `docker compose up -d` for the first time, Docker may have cached the old password volume. Recreate the container and its volume:
   ```bash
   docker compose down -v
   docker compose up -d
   ```
   > [!WARNING]
   > The `-v` flag deletes the database volume, ensuring Postgres re-initializes and re-runs the database seed script with the new credentials.

---

## 3. Docker Container Not Running

### Symptoms
- In the application logs: `sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) connection to server at "localhost" (127.0.0.1), port 5400 failed: Connection refused`.

### Diagnosis & Resolution
1. Check if the Docker daemon is running on your machine:
   ```bash
   docker info
   ```
2. Check if the database container is running:
   ```bash
   docker ps
   ```
3. If no containers are listed, check if the container exists but stopped:
   ```bash
   docker ps -a
   ```
4. Start the database containers:
   ```bash
   docker compose up -d
   ```
5. Check container logs to inspect why it failed to boot:
   ```bash
   docker logs postgres_database
   ```

---

## 4. Missing Environment Variables

### Symptoms
- The application crashes at start or during query execution with `TypeError: ...` or key lookup errors.
- Environment variables resolve to `None`.

### Diagnosis & Resolution
1. Ensure `dotenv` is successfully loading variables. In `app/database.py`, `load_dotenv()` is called at the top.
2. Ensure you are running the application from the root directory of the project, as `dotenv` searches the current working directory for `.env`.
3. You can verify environment loading by printing env vars through a Python shell:
   ```bash
   uv run python -c "import os; from dotenv import load_dotenv; load_dotenv(); print(os.getenv('POSTGRES_DB'))"
   ```

---

## 5. Port 5400 Already In Use

### Symptoms
- When running `docker compose up -d`, you see:
  `Bind for 0.0.0.0:5400 failed: port is already allocated` or `Address already in use`.

### Diagnosis & Resolution
1. Another service (such as a local PostgreSQL server or another Docker container) is already listening on port `5400`.
2. Find the process ID (PID) running on port `5400`:
   ```bash
   # Linux/macOS
   sudo lsof -i :5400
   ```
3. You can stop the conflicting process, or change the exposed host port in `.env` and `docker-compose.yml`:
   - In `.env`, update: `POSTGRES_PORT=5401`
   - In `docker-compose.yml`, change the port mapping line to:
     ```yaml
     ports:
       - 5401:5432
     ```
   - Restart the containers:
     ```bash
     docker compose up -d
     ```

---

## 6. Rate Limit Errors (HTTP 429)

### Symptoms
- Logs show warnings from services like:
  `[SQL Generator] Attempt 1/3 — transient error (ResourceExhausted: 429 Resource has been exhausted...`
- The system pauses and prints a warning that it is waiting to retry.

### Diagnosis & Resolution
1. The Gemini API has rate limits (Requests Per Minute - RPM, Tokens Per Minute - TPM). Under a free-tier API key, these limits are lower.
2. The codebase implements an **automatic exponential backoff retry mechanism** for transient API errors like `429` (Resource Exhausted). The generator, decomposer, and summarizer will sleep and retry after:
   - Attempt 1: 2 seconds
   - Attempt 2: 4 seconds
   - Attempt 3: 8 seconds
3. If errors persist, consider upgrading to a pay-as-you-go account in Google Cloud / AI Studio, or slow down your API requests.

---

## 7. Gemini Service Unavailable (HTTP 503)

### Symptoms
- Logs show errors containing:
  `503 Service Unavailable` or `UNAVAILABLE`.

### Diagnosis & Resolution
1. Google's LLM servers may experience temporary outages or overload.
2. The codebase automatically retries these transient status codes (with exponential backoff) up to 3 times.
3. Check the Google Cloud status page or try again in a few minutes. If it is a persistent service outage, you can monitor the status on public health dashboards.
