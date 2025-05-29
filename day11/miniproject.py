# •	Take user input for name, email, skills, and experience.
# •	Store these as attributes in a class.
# •	Add method to save resume to a .txt file.
# •	Bonus: Integrate with a template or PDF generator.

class miniproject:

    def __init__(self,name,email,skill,experience):
        self.name=name
        self.email=email
        self.skill=skill
        self.experience=experience

    def display(self):
        print(f"Employee Name : {self.name}\n")
        print(f"employee Email : {self.email}\n")
        print("----- Skill -----\n")
        print(f"{self.skill}\n")

        print(f"----- Experience -----\n")
        print(f"{self.experience}\n")

    def save(self,filename="mini.txt"):
        with open(filename,"w") as file:
            file.write("----- Employee Detail -----\n")
            file.write(f"Name : {self.name}\n")
            file.write(f"Email : {self.email}\n\n")
            file.write("----- Skill -----\n")
            for skill in self.skill:
                file.write(f"{skill}\n")
            file.write(f"\n")

            file.write(f"----- Experience -----\n")
            for experience in self.experience:
                file.write(f"{experience}\n")

m=miniproject(

    name="happy",
    email="abc@",
    skill=["python","data analyst","data science"],
    experience=["1 year intern","2 year compony"]

)

m.display()
m.save()

