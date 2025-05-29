class Student:
    def __init__(self, name, roll_no, mark=None):
        self.name = name
        self.roll_no = roll_no
        self.mark = mark if mark else []

    def add_mark(self, mark):
        self.mark.append(mark)

    def average_mark(self):
        if not self.mark:
            return 0
        return sum(self.mark) / len(self.mark)

    def display_info(self):
        print(f"🎓 Name: {self.name}")
        print(f"🆔 Roll No: {self.roll_no}")
        print(f"📊 Marks {self.mark}")
        print(f"📈 Average: {self.average_mark():.2f}")

# Example Usage
student1 = Student("Ankit", "BCA101")
student1.add_mark(88)
student1.add_mark(92)
student1.add_mark(85)
student1.display_info()
