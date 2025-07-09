from unittest.mock import patch
from app.commands import add
from app import storage

def test_add_command(monkeypatch):
    # Capture values passed to insert_log
    called = {}

    def fake_insert_log(title, trigger, action, feeling, intentional):
        called["title"] = title
        called["trigger"] = trigger
        called["action"] = action
        called["feeling"] = feeling
        called["intentional"] = intentional

    # Patch where it's used, not where it's defined
    monkeypatch.setattr("app.commands.add.insert_log", fake_insert_log)

    # Simulate user input
    inputs = iter([
        "Test Habit",     # title
        "Late night",     # trigger
        "Watch YouTube",  # action
        "Tired",          # feeling
        "yes"             # intentional
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Run the handler
    add.handle()

    # Assertions
    assert called["title"] == "Test Habit"
    assert called["trigger"] == "Late night"
    assert called["action"] == "Watch YouTube"
    assert called["feeling"] == "Tired"
    assert called["intentional"] is True
