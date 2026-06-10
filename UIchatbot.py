from dotenv import load_dotenv
load_dotenv()

import streamlit as st

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import (
    AIMessage,
    SystemMessage,
    HumanMessage
)

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Multi Personality AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>
.main {
    background-color: #0E1117;
}

.title {
    text-align: center;
    font-size: 3rem;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: #aaaaaa;
    margin-bottom: 25px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- MODEL ----------------

model = ChatMistralAI(
    model="mistral-small-2603",
    temperature=0.9
)

# ---------------- HEADER ----------------

st.markdown(
    "<h1 class='title'>🤖 Multi Personality AI Chatbot</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p class='subtitle'>Choose your AI personality and start chatting!</p>",
    unsafe_allow_html=True
)

# ---------------- MODES ----------------

modes = {
    "😡 Angry": "You are an angry AI agent. You respond aggressively and impatiently.",

    "😂 Funny": "You are a very funny AI agent. You respond with humor and jokes.",

    "😢 Sad": "You are a very sad AI agent. You respond sadly and emotionally.",

    "💪 Motivational": "You are a motivational coach. Motivate users and encourage them positively.",

    "👨‍🏫 Teacher": "You are an expert teacher. Explain everything in a simple and easy way with examples.",

    "🔥 Roast": "You are a roast master. Give funny and harmless roasts.",

    "❤️ Romantic": "You are a romantic AI. Respond in a sweet, caring and affectionate way.",

    "😎 GenZ": "You are a GenZ AI. Use modern slang, memes and trendy language.",

    "🏴‍☠️ Pirate": "You are a pirate. Speak like a pirate and use pirate vocabulary.",

    "✍️ Shayar": "You are a poet and shayar. Reply using poetry and shayari."
}

selected_mode = st.selectbox(
    "🎭 Select AI Personality",
    list(modes.keys())
)

system_prompt = modes[selected_mode]

# ---------------- SESSION STATE ----------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "mode" not in st.session_state:
    st.session_state.mode = selected_mode

# Reset chat when mode changes
if st.session_state.mode != selected_mode:
    st.session_state.messages = []
    st.session_state.mode = selected_mode

# ---------------- DISPLAY CHAT ----------------

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------- USER INPUT ----------------

prompt = st.chat_input("Type your message...")

if prompt:

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    conversation = [
        SystemMessage(content=system_prompt)
    ]

    for msg in st.session_state.messages:

        if msg["role"] == "user":
            conversation.append(
                HumanMessage(content=msg["content"])
            )
        else:
            conversation.append(
                AIMessage(content=msg["content"])
            )

    response = model.invoke(conversation)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response.content
    })

    st.rerun()

# ---------------- RESET BUTTON ----------------

st.divider()

if st.button("🔄 Reset Chat"):
    st.session_state.messages = []
    st.rerun()

