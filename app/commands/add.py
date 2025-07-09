from app.storage import insert_log

def handle(args=None):
    print("🧠 Let's log your habit loop. Keep it short and real.")

    title = input("📌 Short label for this loop (e.g. 'Mindless Snacking'): ").strip()
    trigger = input("⏱ What led to it? (e.g. 'Watching Netflix after work'): ").strip()
    action = input("🎯 What did you do (or not do)? (e.g. 'Ate chips & scrolled IG'): ").strip()
    feeling = input("💬 How did it make you feel? (e.g. 'Sluggish and annoyed'): ").strip()
    intentional = input("❓ Did you plan to do this? (yes/no): ").strip().lower() in ["yes", "y"]

    insert_log(title, trigger, action, feeling, intentional)
    print("✅ Entry saved.")
