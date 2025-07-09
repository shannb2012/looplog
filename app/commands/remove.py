from app.storage import delete_entry_by_index, get_all_entries

def handle(index):
    entries = get_all_entries()

    if index < 1 or index > len(entries):
        print("❌ Invalid index")
        return

    entry = entries[index - 1]
    confirm = input(f"🗑 Are you sure you want to delete: '{entry['title']}'? (y/n): ").strip().lower()
    if confirm not in ["y", "yes"]:
        print("↩️ Cancelled.")
        return

    delete_entry_by_index(index)
    print(f"✅ Removed: {entry['title']}")
