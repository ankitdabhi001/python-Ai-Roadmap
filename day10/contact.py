# Add new contacts (Name, Phone, Email)

# View all contacts

# Search by name

def add():

    name=input("enter your name : ").strip().title()
    phone=int(input("enter your name  phone number : "))
    email=input("enter your email : ").strip()

    with open("detailbook.txt","a") as file:
        file.write(f"{name},{phone},{email}\n")
        print("contact added ..!")


def show():
    print("Here your details:")

    with open("detailbook.txt", "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 3:
                name, phone, email = parts
                print(f"{name} || {phone} || {email}")
            else:
                print(f"⚠️ Skipping malformed line: {line.strip()}")

def search():

    search_name=input("enter name to find : ").strip().lower()
    found=False

    with open("detailbook.txt","r") as file:    
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 3:
                name, phone, email = parts

                if search_name in name.lower():
                    print(f"{name} | {phone} | {email}")
                    found=True
            else:
                continue

    if not found:
        print("contact is not in your detailbook..!")



while True:

    print("Select Your Choice :")
    print("1.Add contact ")
    print("2.Show your contact")
    print("3.search yor contact")
    print("4.exit")

    choice=int(input("Enter your choice like (1,2,3,4) : "))

    if choice==1:
        add()
    elif choice==2:
        show()
    elif choice==3:
        search()
    elif choice==4:
        break
    else:
        print("invalid choice...!")