import difflib

# Base class
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.name} | {self.phone} | {self.email}"

# Smart child class with AI search
class SmartContact(Contact):
    def __init__(self, name, phone, email, tags=None):
        super().__init__(name, phone, email)
        self.tags = tags if tags else []

    def matches(self, query):
        # Fuzzy match against name and tags
        keywords = [self.name] + self.tags
        return any(difflib.get_close_matches(query, [k.lower() for k in keywords], cutoff=0.6))

# Manager class to store contacts
class ContactBook:
    def __init__(self):
        self.contacts = []

    def add(self, contact):
        self.contacts.append(contact)

    def ai_search(self, query):
        print(f"\n🤖 AI Search Results for: {query}")
        found = False
        for contact in self.contacts:
            if isinstance(contact, SmartContact) and contact.matches(query.lower()):
                print(contact)
                found = True
        if not found:
            print("No close matches found.")

# Example usage
book = ContactBook()
book.add(SmartContact("Ankit Sharma", "1234567890", "ankit@gmail.com", tags=["work", "friend"]))
book.add(SmartContact("Meena Verma", "9876543210", "meena@yahoo.com", tags=["family"]))
book.add(SmartContact("Ravi Kumar", "5555555555", "ravi@xyz.com", tags=["gym", "yoga"]))

# Try AI fuzzy search
book.ai_search("verma")
book.ai_search("fri")
book.ai_search("yogaa")
