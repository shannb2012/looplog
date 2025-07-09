from app.storage import get_all_entries

def handle():
    entries = get_all_entries()

    if not entries:
        print("📭 No habit entries found.")
        return

    print("\n📋 Your Habit Loops:\n")
    for i, entry in enumerate(entries, start=1):
        print(f"{i}. 🌀 {entry['title']}")
        print(f"   ⏱ Trigger: {entry['trigger']}")
        print(f"   🎯 Action: {entry['action']}")
        print(f"   💬 Feeling: {entry['feeling']}")
        print(f"   🤔 Intentional: {'Yes' if entry['intentional'] else 'No'}")
        print(f"   📅 Logged at: {entry['created_at']}\n")
