import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://api.fireworks.ai/inference/v1",
    api_key=os.getenv("FIREWORKS_API_KEY")
)

def ask_ai(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model="accounts/fireworks/models/llama-v3p1-8b-instruct",  # Use your working model
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"❌ OpenAI API error: {e}")
        return None

def suggest_habit_goal(goal: str):
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
