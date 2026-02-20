import streamlit as st
from langchain_community.chat_models import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage

# ==============================
# PAGE CONFIG
# ==============================

st.set_page_config(
    page_title="Life Decision Simulator",
    layout="wide"
)

st.title("🧠 Life Decision Scenario Simulator")
st.caption("Enter a major life decision. AI generates probability-weighted scenario trees.")

# ==============================
# MODEL CONFIG
# ==============================

MODEL_NAME = "qwen2.5:3b"

@st.cache_resource
def load_model():
    return ChatOllama(
        model=MODEL_NAME,
        temperature=0.3
    )

llm = load_model()

# ==============================
# SYSTEM PROMPT
# ==============================

SYSTEM_PROMPT = """
You are a strategic life planning analyst.

When given a life decision, generate a structured scenario tree with probability-weighted outcomes.

Rules:
- Provide 3 primary scenarios (Best Case, Realistic Case, Worst Case).
- Assign realistic probability percentages to each (must total 100%).
- Under each scenario, include:
    - Career Impact
    - Financial Impact
    - Emotional Impact
    - Long-term 5-year outlook
- Be realistic, balanced, and analytical.
- Do NOT give motivational advice.
- Use clean markdown formatting.
"""

# ==============================
# USER INPUT
# ==============================

decision = st.text_area(
    "📌 Enter your life decision:",
    placeholder="Example: Move abroad for a job opportunity"
)

generate = st.button("Generate Scenario Tree")

# ==============================
# GENERATION
# ==============================

if generate:

    if not decision.strip():
        st.warning("Please enter a life decision.")
        st.stop()

    st.subheader("🌳 Scenario Analysis")

    response_placeholder = st.empty()
    full_response = ""

    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=f"Life Decision:\n{decision}")
    ]

    for chunk in llm.stream(messages):
        if chunk.content:
            full_response += chunk.content
            response_placeholder.markdown(full_response + "▌")

    response_placeholder.markdown(full_response)

    st.success("✅ Scenario analysis complete.")