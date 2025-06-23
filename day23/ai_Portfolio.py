import streamlit as st
import json

# ----------------- PAGE CONFIG --------------------
st.set_page_config(page_title="Ankit Dabhi | AI Portfolio", layout="wide")
st.title("👨‍💻 Ankit Dabhi")
st.markdown("### Python + AI Developer | Building Intelligent Tools with LLMs")

# ----------------- ABOUT SECTION --------------------
st.markdown("""
Hi, I'm Ankit — a passionate AI Developer specializing in Python, Streamlit, and LLM-powered tools. 
I love building AI apps that solve real-world problems like resume analyzers, email bots, and script generators.
""")

st.markdown("---")

# ----------------- SKILLS SECTION --------------------
st.subheader("⚙️ Skills")
st.markdown("""
- **Languages:** Python, SQL, JavaScript  
- **AI/ML:** OpenAI API, LLaMA, Transformers, scikit-learn  
- **Libraries:** Streamlit, Pandas, NumPy, Regex  
- **Tools:** Git, GitHub, VS Code, Postman  
- **Deployment:** Streamlit Cloud, Hugging Face Spaces
""")

st.markdown("---")

# ----------------- PROJECTS SECTION --------------------
st.subheader("🚀 Projects")

projects = [
    {
        "title": "AI Note Keeper",
        "description": "A smart note-taking app with AI tagging and natural language search.",
        "tech": ["Python", "Streamlit", "OpenAI API"],
        "github": "https://github.com/ankitdabhi001/ai-note-keeper",
        "demo": "https://huggingface.co/spaces/ankitdabhi001/ai-note-keeper"
    },
    {
        "title": "Resume Analyzer",
        "description": "Parses and analyzes resumes vs job descriptions using regex and NLP.",
        "tech": ["Python", "Regex", "LangChain"],
        "github": "https://github.com/ankitdabhi001/resume-analyzer",
        "demo": ""
    },
    {
        "title": "YouTube Script Generator",
        "description": "AI-powered tool that generates engaging YouTube scripts from topics.",
        "tech": ["Python", "LLaMA", "Streamlit"],
        "github": "https://github.com/ankitdabhi001/youtube-script-writer",
        "demo": ""
    }
]

for proj in projects:
    st.markdown(f"### {proj['title']}")
    st.write(proj['description'])
    st.markdown(f"**Tech Stack:** {', '.join(proj['tech'])}")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"[🔗 GitHub]({proj['github']})")
    with col2:
        if proj['demo']:
            st.markdown(f"[🌐 Live Demo]({proj['demo']})")
    st.markdown("---")

# ----------------- RESUME SECTION --------------------
st.subheader("📄 Resume")

with open("Ankit_Dabhi_Resume_2025.pdf", "rb") as resume_file:
    st.download_button(
        label="📥 Download Resume",
        data=resume_file,
        file_name="Ankit_Dabhi_Resume.pdf",
        mime="application/pdf"
    )

# ----------------- FOOTER --------------------
st.markdown("---")
st.markdown("📫 Reach me at [LinkedIn](https://www.linkedin.com/in/ankitdabhi) or visit my [GitHub](https://github.com/ankitdabhi001)")
