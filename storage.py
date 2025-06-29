import sqlite3
from datetime import datetime

DB_PATH = "looplog.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                title TEXT,
                trigger TEXT,
                action TEXT,
                feeling TEXT,
                intentional BOOLEAN
            );
        """)
        conn.commit()

def insert_log(title, trigger, action, feeling, intentional):
    with get_connection() as conn:
        conn.execute("""
            INSERT INTO logs (timestamp, title, trigger, action, feeling, intentional)
            VALUES (?, ?, ?, ?, ?, ?);
        """, (
            datetime.utcnow().isoformat(),
            title, trigger, action, feeling, intentional
        ))
        conn.commit()

def get_all_logs():
    with get_connection() as conn:
        cursor = conn.execute("SELECT * FROM logs ORDER BY timestamp DESC;")
        return cursor.fetchall()

def get_log_by_index(index):
    logs = get_all_logs()
    try:
        return logs[index - 1]
    except IndexError:
        return None
