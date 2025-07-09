from app.llm import suggest_habit_goal

def handle(args: list):
    if not args:
        print("❌ Please provide a goal to improve (e.g. 'sleep', 'fitness').")
        return

    goal = " ".join(args)
    suggest_habit_goal(goal)