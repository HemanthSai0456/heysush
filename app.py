import streamlit as st
import datetime
import openai

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(page_title="Hey Sush", layout="wide")

# ---------------------------
# Custom CSS
# ---------------------------
st.markdown("""
<style>
    body {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        color: white;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .hero {
        text-align: center;
        padding: 80px 20px;
    }
    .hero h1 {
        font-size: 3.5rem;
        color: #00ffcc;
        text-shadow: 0px 0px 15px rgba(0,255,204,0.8);
    }
    .hero p {
        font-size: 1.2rem;
        color: #f0f0f0;
    }
    .stTextInput, .stTextArea {
        background-color: #2c2c2c;
        color: white;
    }
    .chat-bubble-user {
        background-color: #005b96;
        color: white;
        padding: 10px;
        border-radius: 10px;
        margin: 5px 0px;
        text-align: right;
    }
    .chat-bubble-ai {
        background-color: #333333;
        color: #00ffcc;
        padding: 10px;
        border-radius: 10px;
        margin: 5px 0px;
        text-align: left;
    }
</style>
<div class="hero">
<h1>Hey Sush 🤖</h1>
<p>Your Personal AI Companion – Launching Nov 10</p>
</div>
""", unsafe_allow_html=True)

# ---------------------------
# Countdown
# ---------------------------
launch_date = datetime.date(2025, 11, 10)
today = datetime.date.today()
days_left = (launch_date - today).days
st.markdown(f"### ⏳ Launching in {days_left} days!")

# ---------------------------
# Fake Chat Preview
# ---------------------------
st.markdown("## 💬 Preview Chat")
preview_input = st.text_input("You:", "")
if preview_input:
    st.markdown(f"**You:** {preview_input}")
    st.markdown("**Hey Sush AI:** That’s cool! I can’t wait to chat more after launch 🚀")

# ---------------------------
# Email Signup
# ---------------------------
st.markdown("### 📩 Stay Updated – Get Notified on Launch")
email = st.text_input("Enter your email:")
if st.button("Notify Me"):
    if email:
        with open("emails.csv", "a") as f:
            f.write(email + "\n")
        st.success("Thanks! We'll notify you on launch day 🎉")
    else:
        st.error("Please enter a valid email.")

# ---------------------------
# Chat Section
# ---------------------------
st.subheader("💬 Chat with Hey Sush")
if "messages" not in st.session_state:
    st.session_state["messages"] = []

for role, msg in st.session_state["messages"]:
    bubble_class = "chat-bubble-user" if role == "user" else "chat-bubble-ai"
    st.markdown(f"<div class='{bubble_class}'>{msg}</div>", unsafe_allow_html=True)

chat_input = st.text_input("Type your message here:", key="chat_input")
if st.button("Send"):
    if chat_input:
        st.session_state["messages"].append(("user", chat_input))
        try:
            openai.api_key = st.secrets["OPENAI_API_KEY"]
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": r, "content": m} for r, m in st.session_state["messages"]]
            )
            ai_reply = response.choices[0].message["content"].strip()
        except Exception as e:
            ai_reply = f"(Error: {e})"
        st.session_state["messages"].append(("ai", ai_reply))
        st.experimental_rerun()

# ---------------------------
# Footer
# ---------------------------
st.markdown("""
<hr>
<center>
<p style='color: #aaa;'>Made with ❤️ for Sush | © 2025 Hey Sush AI</p>
</center>
""", unsafe_allow_html=True)
