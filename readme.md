# 🚨 India Multi-Modal Crisis Responder

An AI-powered emergency assistance system designed specifically for India that processes text and images to provide calm, step-by-step crisis guidance in real time.

This system combines a FastAPI backend with an HTML frontend and uses locally running AI models via Ollama for privacy and reliability.

---

## 🇮🇳 India-Specific Emergency Support

The assistant is configured for Indian emergency services:

- **112** → National Emergency Helpline  
- **108** → Ambulance  
- **101** → Fire  
- **100** → Police (112 preferred if unsure)

The AI always encourages contacting emergency services in serious situations.

---

## 🚀 Features

- 📝 Text-based emergency description
- 🖼 Image-based situation analysis (Vision AI)
- 🧠 Crisis-safe prompt engineering
- 🇮🇳 India-specific emergency numbers
- ⚡ FastAPI backend
- 🌐 Lightweight HTML frontend
- 🔒 Fully local execution via Ollama
- 🛡 Safety-first instruction format

---

## 🏗 Architecture

User (Text / Image)  
        ↓  
HTML Frontend  
        ↓  
FastAPI Backend  
        ↓  
Vision Model (LLaVA) → Scene Understanding  
        ↓  
Text Model (Qwen2.5) → Emergency Guidance  
        ↓  
Structured Step-by-Step Response  

---

## 🛠 Tech Stack

- FastAPI
- Uvicorn
- Ollama
- Qwen2.5 (Text LLM)
- LLaVA (Vision Model)
- Python
- HTML + JavaScript

---

## 📦 Installation

### 1️⃣ Install Ollama

Download from:
https://ollama.com

Pull required models:
