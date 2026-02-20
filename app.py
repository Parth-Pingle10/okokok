import streamlit as st
from langchain_community.chat_models import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage

# ==============================
# CONFIG
# ==============================
st.set_page_config(page_title="Digital Habit Architect", layout="centered")
st.title("🧠 Digital Habit Architect")
st.caption("Break bad habits using a 5-step Tiny Habits system")

MODEL_NAME = "qwen2.5:3b"

# ==============================
# LOAD MODEL
# ==============================
@st.cache_resource
def load_model():
    return ChatOllama(
        model=MODEL_NAME,
        temperature=0.6
    )

llm = load_model()

# ==============================
# USER INPUT
# ==============================
bad_habit = st.text_input("What bad habit do you want to break? (e.g., Phone scrolling)")
goal = st.text_input("What is your goal instead? (e.g., Read 20 minutes daily)")

generate = st.button("Build My Habit Plan")

# ==============================
# GENERATE PLAN
# ==============================
if generate:

    if not bad_habit or not goal:
        st.warning("Please enter both your bad habit and your goal.")
        st.stop()

    system_prompt = f"""
You are a behavioral psychology expert specializing in Tiny Habits methodology.

The user wants to stop: {bad_habit}
Their goal is: {goal}

Generate a practical 5-step Tiny Habits plan.

Rules:
- Each step must be small and easy
- Focus on triggers and environment design
- Include replacement behavior
- Keep it realistic and sustainable
- Use clear step-by-step format
- Encourage positive reinforcement
"""

    st.subheader("📋 Your 5-Step Tiny Habit Plan")

    response_placeholder = st.empty()
    full_response = ""

    for chunk in llm.stream([
        SystemMessage(content=system_prompt),
        HumanMessage(content="Generate the plan.")
    ]):
        if chunk.content:
            full_response += chunk.content
            response_placeholder.markdown(full_response + "▌")

    response_placeholder.markdown(full_response)