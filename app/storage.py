import sqlite3
from pathlib import Path

DB_PATH = Path("looplog.db")

def get_connection():
    return sqlite3.connect(DB_PATH)

def initialize():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS habits (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                trigger TEXT,
                action TEXT NOT NULL,
                feeling TEXT,
                intentional INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()

def insert_log(title, trigger, action, feeling, intentional):
    with get_connection() as conn:
        conn.execute("""
            INSERT INTO habits (title, trigger, action, feeling, intentional)
            VALUES (?, ?, ?, ?, ?)
        """, (title, trigger, action, feeling, int(intentional)))
        conn.commit()


def get_all_entries():
    with get_connection() as conn:
        cursor = conn.execute("""
            SELECT id, title, trigger, action, feeling, intentional, created_at
            FROM habits
            ORDER BY created_at DESC
        """)
        rows = cursor.fetchall()

    return [
        {
            "id": row[0],
            "title": row[1],
            "trigger": row[2],
            "action": row[3],
            "feeling": row[4],
            "intentional": bool(row[5]),
            "created_at": row[6],
        }
        for row in rows
    ]

def delete_entry_by_index(index):
    with get_connection() as conn:
        cursor = conn.execute("SELECT id FROM habits ORDER BY created_at DESC")
        rows = cursor.fetchall()

        if index < 1 or index > len(rows):
            return

        entry_id = rows[index - 1][0]
        conn.execute("DELETE FROM habits WHERE id = ?", (entry_id,))
        conn.commit()

