# Basic Parent and Child class demo
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def display(self):
        print(f"{self.name} | {self.phone}")

class SmartContact(Contact):
    def __init__(self, name, phone, tags=[]):
        super().__init__(name, phone)
        self.tags = tags

    def display(self):
        super().display()
        print(f"Tags: {', '.join(self.tags)}")

# Usage
c1 = SmartContact("Ankit", "9876543210", tags=["friend", "python"])
c1.display()
