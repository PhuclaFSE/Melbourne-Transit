import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

dbname = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
host = os.getenv("DB_HOST")
password = os.getenv("DB_PASSWORD")
port = os.getenv("DB_PORT")

dir = os.path.dirname(__file__)
tables = ["calendar", "calendar_dates", "stops", "routes", "trips", "stop_times"]

try:
    conn = psycopg2.connect(database=dbname, user=user, host=host, password=password, port=port)
    with conn.cursor() as cur:
        print("[DB] Creating schema melbournetransit...")

        cur.execute("""
            CREATE EXTENSION IF NOT EXISTS postgis;
            DROP SCHEMA IF EXISTS melbournetransit CASCADE;
            CREATE SCHEMA melbournetransit;
        """)
        print("\n[DB] Created schema melbournetransit")
        for table in tables:
            print(f"[DB] Creating table {table}...")
            path = os.path.join(dir, f"main/{table}.sql")
            with open(path, "r") as file:
                script = file.read()
            cur.execute(script)
            print(f"\n[DB] Created table {table}")
    conn.commit()
    print("[DB] Successfully created database structure")

except Exception as e:
    print(f"[ERR] {e}")
    if "conn" in locals():
        conn.rollback()

finally:
    if "conn" in locals():
        conn.close()



