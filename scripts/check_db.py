import sqlite3

conn = sqlite3.connect("bluestock_mf.db")
cursor = conn.cursor()

for table in ["nav_history", "investor_transactions", "scheme_performance"]:
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    count = cursor.fetchone()[0]
    print(f"{table}: {count} rows")

conn.close()