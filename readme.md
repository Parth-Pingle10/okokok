# 🧠 Digital Habit Architect

Break bad habits using a science-backed 5-Step Tiny Habits system powered by a local LLM (Ollama + LangChain + Streamlit).

## 🚀 Overview
Digital Habit Architect is a Streamlit-based AI app that helps users:
- Identify a bad habit
- Define a positive replacement goal
- Generate a realistic 5-step Tiny Habits action plan
- Focus on triggers and environment design
- Encourage positive reinforcement

The app runs fully locally using Ollama (`qwen2.5:3b`) for private and efficient AI generation.

## 🛠️ Tech Stack
- Streamlit
- LangChain
- Ollama
- Qwen2.5:3B
- Python

## 📦 Installation

### Clone the Repository
git clone https://github.com/yourusername/digital-habit-architect.git  
cd digital-habit-architect

### Install Dependencies
pip install streamlit langchain langchain-community ollama

### Install Ollama
Download from https://ollama.com

### Pull Model
ollama pull qwen2.5:3b

## ▶️ Run the App
streamlit run app.py

Open in browser:
http://localhost:8501

## 🧠 How It Works
1. User enters a bad habit and a replacement goal.
2. The app sends a structured behavioral psychology prompt.
3. The local LLM generates a 5-step Tiny Habits plan.
4. Response is streamed live in the UI.

## 🏗️ Architecture
User Input → Streamlit UI → LangChain → Ollama → Qwen2.5 Model

## ⚙️ Configuration
To change model:
MODEL_NAME = "qwen2.5:3b"

## 🔐 Privacy
- Fully local execution
- No external API calls
- No data storage

## 📄 License
MIT License