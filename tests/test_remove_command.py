from unittest.mock import patch
from app.commands import remove

def test_remove_command_valid(monkeypatch):
    logs = [
        {"title": "A"},
        {"title": "B"},
        {"title": "C"}
    ]

    deleted = {}

    monkeypatch.setattr("app.commands.remove.get_all_entries", lambda: logs)
    monkeypatch.setattr("builtins.input", lambda _: "y")
    monkeypatch.setattr("app.commands.remove.delete_entry_by_index", lambda i: deleted.setdefault("deleted", i))

    remove.handle(2)
    assert deleted["deleted"] == 2

def test_remove_command_cancel(monkeypatch):
    logs = [{"title": "A"}]
    monkeypatch.setattr("app.commands.remove.get_all_entries", lambda: logs)
    monkeypatch.setattr("builtins.input", lambda _: "n")

    called = {"deleted": False}

    def fake_delete(index):
        called["deleted"] = True

    monkeypatch.setattr("app.commands.remove.delete_entry_by_index", fake_delete)
    remove.handle(1)

    assert called["deleted"] is False
