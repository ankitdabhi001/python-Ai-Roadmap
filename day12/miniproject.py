
# Smart Contact Search or Add
contacts = []

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def matches(self, query):
        return query.lower() in self.name.lower()

class SmartContact(Contact):
    def __init__(self, name, phone, tags=[]):
        super().__init__(name, phone)
        self.tags = tags

    def matches(self, query):
        return super().matches(query) or query.lower() in [t.lower() for t in self.tags]

    def display(self):
        print(f"{self.name} | {self.phone} | Tags: {', '.join(self.tags)}")

# Add contacts
contacts.append(SmartContact("Ankit Sharma", "9998887777", ["python", "friend"]))
contacts.append(SmartContact("Ravi Verma", "8889990000", ["work", "ML"]))

# Search
query = input("Search contact: ")
for c in contacts:
    if c.matches(query):
        c.display()
