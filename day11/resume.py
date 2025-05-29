import streamlit as st

class ResumeBuilder:
    def __init__(self, name, email, skills, experience):
        self.name = name
        self.email = email
        self.skills = skills
        self.experience = experience

    def display(self):
        st.write(f"👤 **Name:** {self.name}")
        st.write(f"📧 **Email:** {self.email}")
        st.write("💼 **Skills:**")
        for skill in self.skills:
            st.write(f" - {skill}")
        st.write("📜 **Experience:**")
        for job in self.experience:
            st.write(f" - {job}")

    def save_to_file(self, filename="resume.txt"):
        with open(filename, "w") as file:
            file.write(f"Name: {self.name}\n")
            file.write(f"Email: {self.email}\n")
            file.write("Skills:\n")
            for skill in self.skills:
                file.write(f"- {skill}\n")
            file.write("Experience:\n")
            for job in self.experience:
                file.write(f"- {job}\n")
        st.success(f"✅ Resume saved to {filename}")

def main():
    st.title("ResumeBuilder AI")

    # Input fields
    name = st.text_input("Enter your name")
    email = st.text_input("Enter your email")

    skills_input = st.text_area("Enter your skills (comma separated)")
    experience_input = st.text_area("Enter your experience (comma separated)")

    if st.button("Build Resume"):
        if not name or not email:
            st.error("Please enter both your name and email.")
            return

        skills = [skill.strip() for skill in skills_input.split(",") if skill.strip()]
        experience = [exp.strip() for exp in experience_input.split(",") if exp.strip()]

        resume = ResumeBuilder(name, email, skills, experience)

        st.header("Here is your resume:")
        resume.display()

        resume.save_to_file("resume.txt")

        # Bonus: Let user download the resume.txt file
        with open("resume.txt", "r") as file:
            resume_text = file.read()
        st.download_button(label="Download Resume", data=resume_text, file_name="resume.txt", mime="text/plain")

if __name__ == "__main__":
    main()


