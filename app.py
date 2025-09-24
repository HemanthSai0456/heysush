import streamlit as st
import datetime

# App Title
st.title("✨ Welcome to Hey Sush ✨")
st.write("Your personal AI companion, launching **November 10, 2025**.")

# Countdown
launch_date = datetime.date(2025, 11, 10)
today = datetime.date.today()
days_left = (launch_date - today).days
st.metric("⏳ Days to Launch", f"{days_left} days")

# Sneak Peek Chat
st.subheader("👀 Sneak Peek Chat")
st.chat_message("user").markdown("Hey Sush, are you there?")
st.chat_message("assistant").markdown("👋 Hi! I’m getting ready… see you on Nov 10.")

# Email Signup
st.subheader("📩 Get Early Access")
email = st.text_input("Enter your email:")

if st.button("Notify Me"):
    if email:
        with open("emails.csv", "a") as f:
            f.write(email + "\n")
        st.success("Thanks! We'll notify you at launch 🚀")
    else:
        st.error("Please enter a valid email")
