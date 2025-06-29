# 🌀 LoopLog

**LoopLog** is a minimalist, AI-enhanced CLI app for logging and analyzing your daily habit loops. Inspired by behavior change frameworks like Charles Duhigg's _The Power of Habit_, it helps you track the triggers, actions, and feelings tied to your habits — and reflect on them over time.

---

## ✨ Features

- 📥 Add habit loop entries (trigger, action, feeling, etc.)
- 🧠 AI-powered suggestions for new habit goals
- 📋 View a list of all your entries
- 🧪 Analyze habit patterns with simple queries
- 🧠 Built with Python + SQLite + OpenAI/Fireworks API

---

## 🚀 Getting Started

### 1. Clone the repo

git clone https://github.com/shannb2012/looplog.git
cd looplog

### 2. Create a virtual environment

python3 -m venv venv
source venv/bin/activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Create your .env file

OPENAI_API_KEY=your_openai_or_fireworks_api_key_here
⚠️ This file is gitignored — do not share your API key publicly.

### 🧠 Usage

Run the CLI app with:
python looplog.py

### 📌 Available Commands

| Command                 | Description                           |
| ----------------------- | ------------------------------------- |
| `add`                   | Add a new habit loop                  |
| `list`                  | View your logged entries              |
| `ai suggest-habit-goal` | Let AI suggest a new habit goal       |
| `analyze`               | Summarize common themes in your loops |

### Example:

python looplog.py add
python looplog.py ai suggest-habit-goal

### 🛠 Project Structure

looplog/
├── looplog.py # Main CLI app
├── storage.py # SQLite logic
├── .env # API key (not checked into Git)
├── looplog.db # Habit logs database
├── requirements.txt
└── README.md

### 🧩 Future Plans

-Habit success tracking & stats

-Auto-summarization of daily logs

-Cloud sync + multi-device CLI

-Optional web frontend

### 🤝 Contributing

This is a personal project in progress. Feel free to fork, suggest features, or build on top of it!
