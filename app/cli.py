import argparse
from app.commands import add, list_cmd, remove, analyze, ai_suggest
from app.storage import initialize
initialize()

def main():
    parser = argparse.ArgumentParser(description="LoopLog CLI")

    subparsers = parser.add_subparsers(dest="command")

    # Regular commands
    subparsers.add_parser("list")

    subparsers.add_parser("add")

    rm_parser = subparsers.add_parser("remove")
    rm_parser.add_argument("index", type=int)

    complete_parser = subparsers.add_parser("complete")
    complete_parser.add_argument("index", type=int)

    analyze_parser = subparsers.add_parser("analyze")

    # AI commands
    ai_parser = subparsers.add_parser("ai")
    ai_subparsers = ai_parser.add_subparsers(dest="ai_command")
    ai_subparsers.add_parser("suggest-habit-goal")

    args = parser.parse_args()

    # Routing
    if args.command == "add":
        add.handle(args)
    elif args.command == "list":
        list_cmd.handle()
    elif args.command == "remove":
        remove.handle(args.index)
    elif args.command == "complete":
        complete.handle(args.index)
    elif args.command == "analyze":
        analyze.handle()
    elif args.command == "ai":
        if args.ai_command == "suggest-habit-goal":
            ai_suggest.handle()
        else:
            print("🤖 Unknown AI command")
    else:
        parser.print_help()
