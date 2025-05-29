class ResumeBuilder:
    def __init__(self, name, skills=None, experience=None):
        self.name = name
        self.skills = skills if skills else []
        self.experience = experience if experience else []

    def add_skill(self, skill):
        self.skills.append(skill)

    def add_experience(self, job):
        self.experience.append(job)

    def generate_resume(self):
        resume = f"RESUME\n{'='*30}\n"
        resume += f"Name: {self.name}\n\n"

        resume += "Experience:\n"
        for exp in self.experience:
            resume += f"  - {exp}\n"
        resume += "\n"

        resume += "Skills:\n"
        for skill in self.skills:
            resume += f"  - {skill}\n"
        resume += "\n"

        return resume

    def save_to_file(self, filename="ankit_resume.txt"):
        resume_content = self.generate_resume()
        with open(filename, "w") as file:
            file.write(resume_content)
        print(f"Resume saved to {filename}")


# Create a resume
resume = ResumeBuilder("Ankit Sharma")
resume.add_skill("Python")
resume.add_skill("Machine Learning")
resume.add_experience("Intern at OpenAI")
resume.add_experience("Data Science Bootcamp")

# Generate and save
print(resume.generate_resume())
resume.save_to_file("ankit_resume.txt")
