from database import engine

try:
    conn = engine.connect()
    print("Database connected successfully")
    conn.close()
except Exception as e:
    print(f"Error connecting to the database: {e}")
