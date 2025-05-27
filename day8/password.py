import getpass

# --- Initialize the Vault ---
vault = {
    "gmail": ("ankit@gmail.com", "myGmailPass"),
    "github": ("ankitdev", "gitSecure123")
}

# --- Functions ---

def add_entry():
    site = input("Enter site name: ").lower()
    username = input("Enter username/email: ")
    password = getpass.getpass("Enter password (hidden): ")
    vault[site] = (username, password)
    print(f"✅ Entry added for {site}.")

def view_entry():
    site = input("Enter site to retrieve: ").lower()
    if site in vault:
        user, pwd = vault[site]
        print(f"🔐 Username: {user}\n🔑 Password: {pwd}")
    else:
        print("❌ No entry found for that site.")

def show_all_sites():
    if not vault:
        print("🚫 Vault is empty.")
    else:
        print("📁 Sites in vault:")
        for site in vault:
            print(f"🔹 {site}")

# --- Main Menu ---
def password_vault():
    print("🔐 Welcome to Secure Password Vault")
    while True:
        print("\n1. Add New Entry\n2. View Password\n3. Show All Sites\n4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_entry()
        elif choice == "2":
            view_entry()
        elif choice == "3":
            show_all_sites()
        elif choice == "4":
            print("🔒 Vault closed. Stay secure!")
            break
        else:
            print("❗ Invalid choice. Try again.")

# --- Run the Vault ---
password_vault()
