import streamlit as st

# Page configuration
st.set_page_config(page_title="HR Onboarding Bot", page_icon="🤖")

# App title
st.title("🤖 HR Onboarding Assistant")
st.subheader("Welcome to TechNova Solutions!")

# Input fields
name = st.text_input("What's your name?")
age = st.number_input("How old are you?", min_value=10, max_value=100, step=1)
skills = st.text_input("What tech skills do you have? (e.g., Python, HTML, AI)")

# Role & path assignment logic
def suggest_role(skills):
    skills = skills.lower()
    if "python" in skills and "ai" in skills:
        return "AI Developer", "Advanced Python + AI Projects"
    elif "html" in skills or "web" in skills:
        return "Web Developer", "Frontend + Backend Web Projects"
    elif "data" in skills or "excel" in skills:
        return "Data Analyst", "Data Cleaning + Visualization"
    else:
        return "Trainee Developer", "Core Python + Git + Project Building"

# Show result on button click
if st.button("Generate Onboarding Suggestion"):
    if name and age and skills:
        role, path = suggest_role(skills)

        st.success("✅ Onboarding Complete!")
        st.markdown(f"🎉 Welcome aboard, **{name}**!")
        st.markdown(f"🧠 Based on your skills, we suggest the role of: **{role}**")
        st.markdown(f"📚 Your learning path: **{path}**")
        st.info("🚀 Let’s build the future together at TechNova!")
        st.caption("💡 'The best way to predict the future is to invent it.' – Alan Kay")
    else:
        st.warning("Please fill out all fields above.")

