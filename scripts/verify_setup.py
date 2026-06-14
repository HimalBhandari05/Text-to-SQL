#!/usr/bin/env python
"""
Verification Script for Text-to-SQL system setup.
Tests the environment configuration, PostgreSQL database connection,
and Gemini API access to ensure developers can run the system immediately.
"""

import sys
import os
from dotenv import load_dotenv

# Ensure we can load logger and database packages
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "app"))

from logger import get_logger

logger = get_logger("setup_verification")

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"


def check_env():
    """Verifies that .env exists and loads necessary parameters."""
    print("Checking environment configuration...")
    if not os.path.exists(".env"):
        print(f"{RED}✗ Error: .env file is missing!{RESET}")
        print("Please copy .env.example to .env and fill in the values.")
        return False

    load_dotenv()

    required_vars = [
        "GOOGLE_API_KEY",
        "POSTGRES_USER",
        "POSTGRES_PASSWORD",
        "POSTGRES_DB",
        "POSTGRES_HOST",
        "POSTGRES_PORT",
    ]

    missing = []
    for var in required_vars:
        if not os.getenv(var):
            missing.append(var)

    if missing:
        print(f"{RED}✗ Error: Missing variables in .env: {', '.join(missing)}{RESET}")
        return False

    print(f"{GREEN}✓ Environment variables loaded successfully.{RESET}")
    return True


def check_database():
    """Verifies PostgreSQL connectivity and tables seeding status."""
    print("\nChecking PostgreSQL database connection...")
    try:
        from sqlalchemy import create_engine, text

        db_url = (
            f"postgresql://{os.getenv('POSTGRES_USER')}:"
            f"{os.getenv('POSTGRES_PASSWORD')}@"
            f"{os.getenv('POSTGRES_HOST')}:"
            f"{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
        )

        engine = create_engine(db_url, connect_args={"connect_timeout": 5})

        with engine.connect() as conn:
            # Check basic connection
            res = conn.execute(text("SELECT 1"))
            res.fetchone()
            print(f"{GREEN}✓ Connected to PostgreSQL successfully.{RESET}")

            # Check if ClassicModels tables are seeded
            tables = [
                "productlines",
                "products",
                "offices",
                "employees",
                "customers",
                "payments",
                "orders",
                "orderdetails",
            ]
            missing_tables = []
            for table in tables:
                try:
                    count_res = conn.execute(text(f'SELECT COUNT(*) FROM "{table}"'))
                    count = count_res.fetchone()[0]
                    print(f"  - Table '{table}': {count} records found.")
                except Exception:
                    missing_tables.append(table)

            if missing_tables:
                print(
                    f"{RED}✗ Database is connected, but some tables are missing: {', '.join(missing_tables)}{RESET}"
                )
                print("Make sure you let docker-compose seed the database completely.")
                return False

            print(f"{GREEN}✓ Database schema and data are correctly seeded.{RESET}")
            return True

    except Exception as e:
        print(f"{RED}✗ Database connection failed: {e}{RESET}")
        print("Suggestions:")
        print("  1. Run 'docker ps' to check if the 'postgres_database' container is running.")
        print("  2. Check port conflicts on port 5400.")
        print("  3. Verify host credentials in your .env file.")
        return False


def check_gemini():
    """Verifies Gemini API client access and API key viability."""
    print("\nChecking Gemini API client connection...")
    try:
        from google import genai

        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key or api_key == "your_google_api_key":
            print(f"{RED}✗ Error: Google API Key is not configured.{RESET}")
            return False

        client = genai.Client(api_key=api_key)
        # Call a very small test prompt
        response = client.models.generate_content(
            model="gemini-2.5-flash", contents="Respond with 'ok'"
        )

        if "ok" in response.text.lower():
            print(f"{GREEN}✓ Gemini API connected and verified successfully.{RESET}")
            return True
        else:
            print(
                f"{RED}✗ Gemini connection succeeded, but returned unexpected response: '{response.text}'{RESET}"
            )
            return False

    except Exception as e:
        print(f"{RED}✗ Gemini API call failed: {e}{RESET}")
        print("Suggestions:")
        print("  1. Verify the validity of GOOGLE_API_KEY in .env.")
        print("  2. Check your network connection.")
        print("  3. Run again. If rate-limited (429) or offline (503), try later.")
        return False


def main():
    print("==================================================")
    print("      TEXT-TO-SQL SYSTEM CONFIGURATION CHECK      ")
    print("==================================================\n")

    env_ok = check_env()
    if not env_ok:
        sys.exit(1)

    db_ok = check_database()
    gemini_ok = check_gemini()

    print("\n==================================================")
    if db_ok and gemini_ok:
        print(f"{GREEN}SUCCESS: The system is ready to be run!{RESET}")
        print("Run the FastAPI server using:")
        print("  uv run uvicorn app.main:app --reload --port 8001")
        sys.exit(0)
    else:
        print(f"{RED}FAILURE: Setup is incomplete. Please fix the errors above.{RESET}")
        sys.exit(1)


if __name__ == "__main__":
    main()
