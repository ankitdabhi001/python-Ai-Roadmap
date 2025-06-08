
# Mini Project of Resume Builder 
class ResumeBuilder:
    def __init__(self, name, email, skills, experience):
        self.name = name
        self.email = email
        self.skills = skills
        self.experience = experience

    def display(self):
        print(f"👤 Name: {self.name}")
        print(f"📧 Email: {self.email}")
        print("💼 Skills:")
        for skill in self.skills:
            print(f" - {skill}")
        print("📜 Experience:")
        for job in self.experience:
            print(f" - {job}")

    def save_to_file(self, filename="practice.txt"):
        with open(filename, "w") as file:
            file.write(f"Name: {self.name}\n")
            file.write(f"Email: {self.email}\n")
            file.write("Skills:\n")
            for skill in self.skills:
                file.write(f"- {skill}\n")
            file.write("Experience:\n")
            for job in self.experience:
                file.write(f"- {job}\n")
        print(f"✅ Resume saved to {filename}")


# Input from user
name = input("Enter your name: ")
email = input("Enter your email: ")

# Split user input into list items
skills = input("Enter your skills (comma-separated): ").split(",")
skills = [skill.strip() for skill in skills]  # Clean up spaces

experience = input("Enter your experience (comma-separated): ").split(",")
experience = [job.strip() for job in experience]

# Create resume object and run methods
r = ResumeBuilder(name, email, skills, experience)
r.display()
r.save_to_file()
