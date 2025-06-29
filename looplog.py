from storage import init_db, insert_log, get_all_logs, get_log_by_index
import argparse
import json
import os
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

LOG_FILE = Path("logs.json")

client = OpenAI(
    api_key=os.getenv("FIREWORKS_API_KEY"),
    base_url="https://api.fireworks.ai/inference/v1"
)

# === Storage Helpers ===
def load_logs():
    if LOG_FILE.exists():
        with open(LOG_FILE, "r") as f:
            content = f.read().strip()
            return json.loads(content) if content else []
    return []

def save_logs(logs):
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)

# === CLI Commands ===
def new_log():
    print("🧠 Let's log your habit loop. Keep it short and real.")

    title = input("📌 Short label for this loop (e.g. 'Mindless Snacking'): ").strip()
    trigger = input("⏱ What led to it? (e.g. 'Watching Netflix after work'): ").strip()
    action = input("🎯 What did you do (or not do)? (e.g. 'Ate chips & scrolled IG'): ").strip()
    feeling = input("💬 How did it make you feel? (e.g. 'Sluggish and annoyed'): ").strip()
    intentional = input("❓ Did you plan to do this? (yes/no): ").strip().lower() in ["yes", "y"]

    insert_log(title, trigger, action, feeling, intentional)
    print("✅ Entry saved.")


def list_logs():
    logs = get_all_logs()
    if not logs:
        print("📭 No entries found.")
        return
    for i, log in enumerate(logs):
        print(f"{i + 1}. {log[2]} ({log[1]})")  # title + timestamp

def show_log(index):
    log = get_log_by_index(index)
    if not log:
        print("❌ Invalid log index.")
        return

    print("\n🧾 Log Details:")
    fields = ["ID", "Timestamp", "Title", "Trigger", "Action", "Feeling", "Intentional"]
    for label, value in zip(fields, log):
        print(f"{label}: {value}")

# === AI Integration ===
def ask_ai(prompt):
    try:
        response = client.chat.completions.create(
            model="accounts/fireworks/models/llama-v3p1-8b-instruct",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"❌ OpenAI API error: {e}")
        return None

def ai_analyze():
    logs = load_logs()
    if not logs:
        print("📭 No logs to analyze.")
        return

    recent_logs = logs[-10:]
    formatted = json.dumps(recent_logs, indent=2)

    prompt = f"""
You are a habit improvement coach. A user has been logging their habit loops.
Each log includes a title, trigger, action (or inaction), emotional state, and whether the event was intentional.

Here are their recent entries:

{formatted}

Please:
- Identify any recurring patterns, positive or negative
- Highlight what’s working well
- Suggest 1–2 small habit loop changes that could improve consistency
"""

    response = ask_ai(prompt)
    if response:
        print("\n🤖 AI Analysis:\n")
        print(response)

def ai_suggest(goal):
    prompt = f"""
You are an expert behavioral coach. The user says:

“I want to get better at: {goal}”

Suggest **one practical micro-habit loop** using the Trigger → Action → Reward framework.
Include:
- A clear trigger (when/where)
- A tiny first action (≤2 minutes effort)
- A meaningful reward
Also mention one common barrier and how to mitigate it.
"""
    response = ask_ai(prompt)
    if response:
        print("\n🤖 AI Suggestion:\n")
        print(response)

# === CLI entrypoint ===
def main():
    init_db()
    parser = argparse.ArgumentParser(description="LoopLog – AI-enhanced Habit Loop Tracker")
    subparsers = parser.add_subparsers(dest="command")

    # Basic commands
    subparsers.add_parser("new", help="Create a new habit log")
    subparsers.add_parser("list", help="List all logs")

    show_parser = subparsers.add_parser("show", help="Show full details of a log")
    show_parser.add_argument("index", type=int)

    # AI commands
    ai_parser = subparsers.add_parser("ai", help="AI-powered features")
    ai_subparsers = ai_parser.add_subparsers(dest="ai_command")

    ai_subparsers.add_parser("analyze", help="Analyze your habit loop patterns")

    suggest_parser = ai_subparsers.add_parser("suggest", help='Get a micro-habit suggestion')
    suggest_parser.add_argument("goal", nargs="+", help='Your habit goal, in quotes if multi-word')

    args = parser.parse_args()

    if args.command == "new":
        new_log()
    elif args.command == "list":
        list_logs()
    elif args.command == "show":
        show_log(args.index)
    elif args.command == "ai":
        if args.ai_command == "analyze":
            ai_analyze()
        elif args.ai_command == "suggest":
            goal_text = " ".join(args.goal)
            ai_suggest(goal_text)
        else:
            print("❌ Unknown AI subcommand")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
