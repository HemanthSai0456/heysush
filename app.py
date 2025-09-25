import streamlit as st
import datetime

# ---------------------------
# Custom CSS for AI look
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
user_input = st.text_input("You:", "")

if user_input:
    st.markdown(f"**You:** {user_input}")
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
# Footer
# ---------------------------

st.markdown("""
<hr>
<center>
<p style='color: #aaa;'>Made with ❤️ for Sush | © 2025 Hey Sush AI</p>
</center>
""", unsafe_allow_html=True)
