class Contact:
    def __init__(self, name, phone, email, tags=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.tags = tags if tags else []

    def __str__(self):
        return f"👤 {self.name} | 📞 {self.phone} | 📧 {self.email} | 🏷️ {', '.join(self.tags)}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"✅ Contact '{contact.name}' added.")

    def view_contacts(self):
        if not self.contacts:
            print("📭 No contacts found.")
        else:
            print("\n📒 Your Contacts:")
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}. {contact}")

    def search_contact(self, keyword):
        results = [c for c in self.contacts if keyword.lower() in c.name.lower()]
        if results:
            print("\n🔍 Search Results:")
            for contact in results:
                print(contact)
        else:
            print("❌ No contact found with that name.")

    def delete_contact(self, name):
        for c in self.contacts:
            if c.name.lower() == name.lower():
                self.contacts.remove(c)
                print(f"🗑️ Contact '{name}' deleted.")
                return
        print("❌ Contact not found.")

    def update_contact(self, name, new_phone=None, new_email=None, new_tags=None):
        for c in self.contacts:
            if c.name.lower() == name.lower():
                if new_phone:
                    c.phone = new_phone
                if new_email:
                    c.email = new_email
                if new_tags:
                    c.tags = new_tags
                print(f"✅ Contact '{name}' updated.")
                return
        print("❌ Contact not found.")




book = ContactBook()

def show_menu():
    print("\n📱 Smart Contact Book Menu:")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Update Contact")
    print("6. Exit")

while True:
    show_menu()
    choice = input("📥 Enter your choice (1-6): ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        tags = input("Tags (comma-separated): ").split(",")
        contact = Contact(name, phone, email, [t.strip() for t in tags])
        book.add_contact(contact)

    elif choice == "2":
        book.view_contacts()

    elif choice == "3":
        keyword = input("🔍 Enter name to search: ")
        book.search_contact(keyword)

    elif choice == "4":
        name = input("Enter name to delete: ")
        book.delete_contact(name)

    elif choice == "5":
        name = input("Enter name to update: ")
        phone = input("New Phone (leave blank to skip): ")
        email = input("New Email (leave blank to skip): ")
        tags = input("New Tags (comma-separated, leave blank to skip): ")
        book.update_contact(name,
                            new_phone=phone if phone else None,
                            new_email=email if email else None,
                            new_tags=[t.strip() for t in tags.split(",")] if tags else None)

    elif choice == "6":
        print("👋 Exiting Smart Contact Book. Goodbye!")
        break

    else:
        print("❌ Invalid choice. Try again.")
