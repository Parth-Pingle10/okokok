import streamlit as st
from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage
from PIL import Image
import base64
import json

st.set_page_config(page_title="India Multi-Modal Crisis Responder", layout="wide")

st.title("🚨 India Multi-Modal Crisis Responder")
st.caption("AI Emergency Assistant (Text + Image) — India")

# ==============================
# MODELS
# ==============================

TEXT_MODEL = "qwen2.5:3b"
VISION_MODEL = "llava"

@st.cache_resource
def load_text_model():
    return ChatOllama(model=TEXT_MODEL, temperature=0.0)

@st.cache_resource
def load_vision_model():
    return ChatOllama(model=VISION_MODEL, temperature=0.0)

llm = load_text_model()
vision_llm = load_vision_model()

# ==============================
# STAGE 1 — RISK CLASSIFIER
# ==============================

RISK_PROMPT = """
You are an emergency triage classifier.

Return ONLY valid JSON:

{
  "breathing_risk": true/false,
  "bleeding_risk": true/false,
  "structural_collapse": true/false,
  "entrapment": true/false,
  "fire_risk": true/false,
  "severity": "Critical" or "Moderate" or "Low"
}

Rules:
- Structural collapse OR entrapment → severity = Critical
- Breathing risk → severity = Critical
- No explanations
- JSON only
"""

# ==============================
# INPUT
# ==============================

text_input = st.text_area("Describe the emergency:")
image_file = st.file_uploader("Upload image (optional)", type=["png","jpg","jpeg"])

if st.button("Get Emergency Guidance"):

    combined_input = text_input.strip() if text_input else ""

    # --------------------------
    # VISION ANALYSIS
    # --------------------------
    if image_file:
        image = Image.open(image_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        image_bytes = image_file.read()
        image_base64 = base64.b64encode(image_bytes).decode("utf-8")

        vision_response = vision_llm.invoke(
            [HumanMessage(
                content="Describe observable emergency risks only. No speculation.",
                additional_kwargs={"images": [image_base64]}
            )]
        )

        combined_input += "\n" + vision_response.content

    if not combined_input:
        st.warning("Please provide emergency details.")
        st.stop()

    # --------------------------
    # STAGE 1 — RISK ANALYSIS
    # --------------------------
    risk_response = llm.invoke([
        SystemMessage(content=RISK_PROMPT),
        HumanMessage(content=combined_input)
    ])

    try:
        risk_data = json.loads(risk_response.content)
    except:
        st.error("Risk classification failed.")
        st.stop()

    severity = risk_data.get("severity", "Critical")

    # --------------------------
    # PLAYBOOK SELECTION
    # --------------------------

    if risk_data.get("structural_collapse") or risk_data.get("entrapment"):
        emergency_number = "112"
        playbook = """
STRUCTURAL COLLAPSE / ENTRAPMENT PROTOCOL:
- Turn off engine immediately.
- Check for fuel smell or smoke.
- Check for heavy bleeding.
- Avoid sudden neck or spine movement.
- Conserve phone battery after calling.
- Use horn briefly every few minutes if safe.
"""
    elif risk_data.get("fire_risk"):
        emergency_number = "101"
        playbook = """
FIRE PROTOCOL:
- Exit immediately if safe.
- Stay low to avoid smoke.
- Do not re-enter vehicle.
"""
    elif risk_data.get("breathing_risk"):
        emergency_number = "108"
        playbook = """
BREATHING EMERGENCY PROTOCOL:
- Check airway.
- Check breathing.
- Begin CPR if not breathing.
"""
    else:
        emergency_number = "112"
        playbook = """
GENERAL CRITICAL INCIDENT PROTOCOL:
- Ensure scene safety.
- Check for bleeding.
- Avoid sudden movement.
"""

    # --------------------------
    # STAGE 2 — DISPATCH RESPONSE
    # --------------------------

    dispatch_prompt = f"""
You are a trained emergency dispatcher in India.

Risk Analysis:
{risk_data}

Use this emergency protocol:
{playbook}

Generate a structured response using:

🚨 SEVERITY LEVEL: {severity}

1️⃣ CALL THIS NUMBER FIRST:
Call {emergency_number} and explain why.

2️⃣ IMMEDIATE HAZARD CHECK:
(Only relevant checks)

3️⃣ IMMEDIATE LIFE-SAVING ACTION:
(Use protocol steps)

4️⃣ STEP-BY-STEP SURVIVAL GUIDANCE:
(Numbered clear steps)

5️⃣ DO NOT:
(Realistic safety warnings only)

No filler. No repetition. Be decisive.
"""

    st.subheader("🚑 Emergency Guidance")

    response_placeholder = st.empty()
    full_response = ""

    for chunk in llm.stream([
        HumanMessage(content=f"Situation:\n{combined_input}\n\n{dispatch_prompt}")
    ]):
        if chunk.content:
            full_response += chunk.content
            response_placeholder.markdown(full_response + "▌")

    response_placeholder.markdown(full_response)

    st.error("⚠ This AI does NOT replace professional emergency services. Call 112 immediately in life-threatening situations.")