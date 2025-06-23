# portfolio.py
import streamlit as st

st.set_page_config(page_title="Ankit's AI Portfolio", layout="centered")

st.title("👨‍💻 Ankit Dabhi – Python + AI Developer")
st.image("ankit.jpg", width=150)  # Optional profile image

st.subheader("💡 About Me")
st.write("Final year BCA | Passionate about Python, AI & Automation")

st.subheader("🚀 Projects")
st.markdown("""
- 🧠 **AI Resume Screener** — Match resumes to job descriptions using OpenAI API  
- 📝 **Note Keeper** — File-based notes app with Streamlit  
- 🔐 **Password Vault** — Credential manager using dictionaries & base64  
""")

st.subheader("🛠️ Skills")
st.write("Python, OpenAI API, Streamlit, Pandas, Regex, Git")

st.subheader("📂 Download Resume")
with open("Ankit_Dabhi_Resume_2025.pdf", "rb") as f:
    st.download_button("📄 Download PDF", f, file_name="ankit_resume.pdf")

st.subheader("🔗 Connect")
st.markdown("[GitHub](https://github.com/ankitdabhi001) | [LinkedIn](https://linkedin.com/in/ankitdabhi)")

