import os
import streamlit as st
from openai import OpenAI
from openai import RateLimitError
from dotenv import load_dotenv

# Load API key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

st.set_page_config(page_title="Hey Hem AI", page_icon="🤖", layout="centered")

# ---------------------------
# Custom CSS for ChatGPT-style UI
# ---------------------------
st.markdown("""
<style>
    body {
        background: #0f172a;
        color: white;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .user-bubble {
        background: #2563eb;
        color: white;
        padding: 10px 15px;
        border-radius: 15px;
        margin: 8px;
        max-width: 70%;
        float: right;
        clear: both;
    }
    .ai-bubble {
        background: #059669;
        color: white;
        padding: 10px 15px;
        border-radius: 15px;
        margin: 8px;
        max-width: 70%;
        float: left;
        clear: both;
    }
    .title {
        text-align: center;
        font-size: 2.5rem;
        color: #00ffcc;
        margin-bottom: 20px;
        text-shadow: 0px 0px 10px rgba(0,255,204,0.7);
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------
# Title
# ---------------------------
st.markdown("<div class='title'>🤖 Hey Hem AI</div>", unsafe_allow_html=True)

# ---------------------------
# Initialize Chat History
# ---------------------------
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "You are Hey Hem AI, a helpful, kind, and fun AI companion."},
        {"role": "assistant", "content": "Hi 👋, I’m Hem...For whom it may concern?"}
    ]

# Display chat history
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.markdown(f"<div class='user-bubble'>{msg['content']}</div>", unsafe_allow_html=True)
    elif msg["role"] == "assistant":
        st.markdown(f"<div class='ai-bubble'>{msg['content']}</div>", unsafe_allow_html=True)

# ---------------------------
# User Input
# ---------------------------
user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state["messages"].append({"role": "user", "content": user_input})
    st.markdown(f"<div class='user-bubble'>{user_input}</div>", unsafe_allow_html=True)

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=st.session_state["messages"],
        )
        reply = response.choices[0].message.content
        st.session_state["messages"].append({"role": "assistant", "content": reply})
        st.markdown(f"<div class='ai-bubble'>{reply}</div>", unsafe_allow_html=True)
    except RateLimitError:
        st.session_state["messages"].append({"role": "assistant", "content": "Oops! hem is too busy now. Please try again later."})
        st.markdown("<div class='ai-bubble'>Oops! hem is too busy now. Please try again later.</div>", unsafe_allow_html=True)
