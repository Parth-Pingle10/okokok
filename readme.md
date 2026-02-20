# 🧠 Life Decision Scenario Simulator

An AI-powered web application that generates structured, probability-weighted scenario trees for major life decisions.

Users input a significant life choice (e.g., “Move Abroad”), and the AI produces:

- 🌳 Three scenario branches (Best Case, Realistic Case, Worst Case)
- 📊 Probability percentages (total = 100%)
- 💼 Career impact analysis
- 💰 Financial impact analysis
- ❤️ Emotional impact analysis
- 🔮 5-year long-term outlook

---

## 🚀 How It Works

1. User enters a major life decision.
2. AI analyzes possible future outcomes.
3. The system generates structured scenario trees with realistic probability weighting.
4. Results are streamed live in clean markdown format.

---

## 🛠 Tech Stack

- Streamlit (Frontend UI)
- Ollama (Local LLM Runtime)
- LangChain
- Qwen 2.5 Model

---

## 📦 Installation

### 1️⃣ Install Ollama
Download from: https://ollama.com

Pull the required model:ollama pull qwen2.5:3b


### 2️⃣ Install Dependencies
pip install -r requirements.txt


### 3️⃣ Run the Application
streamlit run app.py


---

## 📊 Example Use Cases

- Move abroad for a job
- Leave a stable job to start a company
- Pursue higher education
- Invest savings into a new business
- Relocate for personal reasons

---

## ⚠ Disclaimer

This tool provides analytical simulations based on probabilistic reasoning. It does not guarantee real-world outcomes. Users should consult professionals for financial, legal, or medical decisions.

---

## 🔥 Future Enhancements

- Recursive multi-level scenario branching
- Monte Carlo simulation mode
- Visual decision tree graphs
- Risk heatmaps
- Confidence scoring
- Exportable PDF reports
- Save decision history

---

Built for structured life planning, strategic thinking, and analytical decision support.