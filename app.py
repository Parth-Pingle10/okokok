import streamlit as st
from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage
from PIL import Image
import base64

st.set_page_config(page_title="Multi-Modal Crisis Responder", layout="wide")

st.title("🚨 Multi-Modal Crisis Responder")
st.caption("AI emergency assistant for text, voice, and image-based crisis situations")

# ==============================
# MODELS
# ==============================

TEXT_MODEL = "qwen2.5:3b"
VISION_MODEL = "llava"
WHISPER_MODEL = "whisper"

@st.cache_resource
def load_text_model():
    return ChatOllama(model=TEXT_MODEL, temperature=0.2)

@st.cache_resource
def load_vision_model():
    return ChatOllama(model=VISION_MODEL, temperature=0.2)

text_llm = load_text_model()
vision_llm = load_vision_model()

# ==============================
# SAFETY SYSTEM PROMPT
# ==============================

SYSTEM_PROMPT = """
You are an AI Emergency Crisis Response Assistant operating in India.

Your role:
- Provide calm, step-by-step emergency guidance.
- Prioritize immediate safety.
- Use simple, clear language.
- Avoid medical speculation.
- If unsure, say clearly that you are uncertain.

Important:
- In India, advise calling:
    • 112 (National Emergency Helpline)
    • 108 (Ambulance)
    • 101 (Fire)
    • 100 (Police — but prefer 112 when possible)

Always:
- Encourage contacting emergency services for serious situations.
- Give practical first-aid instructions only if safe.
- Never provide dangerous or extreme instructions.
- Keep tone calm and reassuring.

Format:
1. Immediate Action
2. Safety Steps
3. When to Call Emergency Services
4. Additional Precautions
"""

# ==============================
# INPUT SECTION
# ==============================

st.subheader("📝 Describe the Emergency")
text_input = st.text_area("Type what is happening:")

st.subheader("🎤 Voice Input")
audio_file = st.file_uploader("Upload voice recording (optional)", type=["wav", "mp3"])

st.subheader("🖼 Upload Image (Optional)")
image_file = st.file_uploader("Upload accident/injury image", type=["png", "jpg", "jpeg"])

generate = st.button("Get Emergency Guidance")

# ==============================
# PROCESSING
# ==============================

if generate:

    combined_input = ""

    # ---- TEXT ----
    if text_input:
        combined_input += f"\nUser description:\n{text_input}\n"

    # ---- IMAGE ----
    if image_file:
        image = Image.open(image_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        buffered = image_file.read()
        image_base64 = base64.b64encode(buffered).decode("utf-8")

        vision_prompt = "Describe what is happening in this emergency image clearly."

        vision_response = vision_llm.invoke(
            [HumanMessage(content=vision_prompt, additional_kwargs={"images": [image_base64]})]
        )

        combined_input += f"\nImage Analysis:\n{vision_response.content}\n"

    # ---- VOICE (Optional - Placeholder if no local whisper integration) ----
    if audio_file:
        st.warning("Voice transcription requires Whisper integration via Ollama CLI.")
        combined_input += "\nVoice input provided but transcription not implemented in MVP.\n"

    if not combined_input.strip():
        st.warning("Please provide text, voice, or image input.")
        st.stop()

    # ==============================
    # FINAL CRISIS RESPONSE
    # ==============================

    final_prompt = f"""
Situation Details:
{combined_input}

Provide emergency guidance now.
"""

    st.subheader("🚑 Emergency Guidance")

    response_placeholder = st.empty()
    full_response = ""

    for chunk in text_llm.stream([
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=final_prompt)
    ]):
        if chunk.content:
            full_response += chunk.content
            response_placeholder.markdown(full_response + "▌")

    response_placeholder.markdown(full_response)

    st.warning("⚠ This AI does not replace professional emergency services. Call your local emergency number immediately in serious situations.")