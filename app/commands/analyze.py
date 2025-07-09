import json
from app.storage import get_all_entries
from app.llm import ask_ai

def handle():
    entries = get_all_entries()

    if not entries:
        print("📭 No entries to analyze.")
        return

    print("🔍 Analyzing your habit patterns...")

    prompt = f"""
You are a behavioral analysis assistant. Analyze the following habit loops and identify:
- Recurring triggers
- Common actions
- Emotional patterns (especially negative ones)
- Suggestions for behavior change or reflection
- Highlight what’s working well
- Suggest 1–2 small habit loop changes that could improve consistency

Here is the data:
{json.dumps(entries, indent=2)}
"""

    analysis = ask_ai(prompt)
    if analysis:
        print("\n🧠 AI Habit Analysis:\n")
        print(analysis)
