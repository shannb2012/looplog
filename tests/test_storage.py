import os
import sqlite3
import tempfile
import pytest
from app import storage

@pytest.fixture
def temp_db(monkeypatch):
    # Create a temporary file for the SQLite DB
    db_fd, db_path = tempfile.mkstemp()
    monkeypatch.setattr(storage, "DB_PATH", db_path)
    storage.initialize()
    yield db_path
    os.close(db_fd)
    os.remove(db_path)

def test_insert_and_get_entry(temp_db):
    storage.insert_log("Test Habit", "Evening", "Scrolling", "Tired", True)
    entries = storage.get_all_entries()

    assert len(entries) == 1
    entry = entries[0]
    assert entry["title"] == "Test Habit"
    assert entry["trigger"] == "Evening"
    assert entry["action"] == "Scrolling"
    assert entry["feeling"] == "Tired"
    assert entry["intentional"] is True

def test_delete_entry(temp_db):
    # Add two logs
    storage.insert_log("Habit 1", "Trigger 1", "Action 1", "Feeling 1", True)
    storage.insert_log("Habit 2", "Trigger 2", "Action 2", "Feeling 2", False)

    entries_before = storage.get_all_entries()
    assert len(entries_before) == 2

    # Delete the most recent (index 1)
    storage.delete_entry_by_index(2)

    entries_after = storage.get_all_entries()
    assert len(entries_after) == 1
    assert entries_after[0]["title"] == "Habit 1"
