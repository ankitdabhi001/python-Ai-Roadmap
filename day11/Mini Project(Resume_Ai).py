from fpdf import FPDF
from datetime import datetime
import os

class ResumeBuilder:
    def __init__(self, name, email, phone, skills, experience):
        self.name = name
        self.email = email
        self.phone = phone
        self.skills = skills
        self.experience = experience

    def generate_pdf(self, filename="resume.pdf"):
        pdf = FPDF()
        pdf.add_page()

        # ✅ Add Unicode-compatible font
        font_path = os.path.join("fonts", "DejaVuSans.ttf")
        pdf.add_font("DejaVu", "", font_path, uni=True)
        pdf.set_font("DejaVu", "", 16)

        # 📄 Header
        pdf.cell(200, 10, txt="📄 RESUME", align='C')
        pdf.ln(10)
        pdf.set_font("DejaVu", "", 12)
        pdf.cell(200, 10, txt=f"Generated on: {datetime.now().strftime('%Y-%m-%d')}", align='C')
        pdf.ln(15)

        # 👤 Name & Contact
        pdf.set_font("DejaVu", "", 14)
        pdf.cell(200, 10, txt=self.name)
        pdf.ln(8)
        pdf.set_font("DejaVu", "", 12)
        pdf.cell(200, 10, txt=f"📧 {self.email} | 📞 {self.phone}")
        pdf.ln(15)

        # 🛠️ Skills
        pdf.set_font("DejaVu", "", 12)
        pdf.cell(200, 10, txt="🛠️ Skills:")
        pdf.ln(8)
        for skill in self.skills:
            pdf.cell(200, 8, txt=f"• {skill.strip()}")
            pdf.ln(6)

        pdf.ln(10)

        # 💼 Experience
        pdf.set_font("DejaVu", "", 12)
        pdf.cell(200, 10, txt="💼 Experience:")
        pdf.ln(8)
        for exp in self.experience:
            pdf.multi_cell(0, 8, txt=f"• {exp.strip()}")

        # 📥 Save PDF
        pdf.output(filename)
        print(f"\n✅ Resume saved as: {filename}")

# --------- Run ----------
if __name__ == "__main__":
    print("👤 Enter your resume details:")
    name = input("Full Name: ")
    email = input("Email: ")
    phone = input("Phone Number: ")

    print("\n🛠️ Enter your skills (comma-separated):")
    skills = input("Skills: ").split(',')

    print("\n💼 Enter your experience (one per line, type 'done' to finish):")
    experience = []
    while True:
        line = input("> ")
        if line.lower() == "done":
            break
        experience.append(line)

    resume = ResumeBuilder(name, email, phone, skills, experience)
    resume.generate_pdf(f"{name.replace(' ', '_')}_Resume.pdf")
