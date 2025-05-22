# contact app

contact ={}

def add_contact(name,phone,email):
    contact[name]={"phone":phone,"email":email}
    print(f"{name} contact is added..!")

def find_contact(name):
    if name in contact:
        print(f"{name} ||  {contact[name]['phone']} || {contact[name]['email']}")
    else:
        print("no contact found")

def delete_contact(name):
   if name in contact:
        del contact[name]
        print(f"{name}")

def show_contact():
    if contact:
        for name,info in contact.items():

            print(f"{name} || {info['phone']} || {info['email']}")
    else:
        print("no contact")





while True:
    print("1.add contat")
    print("2.find")
    print("3.delete")
    print("4.show")
    print("5.exit")

    choice=int(input("enter your choice like : 1,2,3,4,5 : "))

    if choice==1:
        name=input("enter contact name : ")
        phone=int(input("enter phone number : "))
        email=input("enter your email : ")
        add_contact(name,phone,email)
    
    elif choice==2:
        name = input("Enter name to search: ")
        find_contact(name)

    elif choice==3:
        name = input("Enter name to delete: ")
        delete_contact(name)

    elif choice==4:
        show_contact()


    elif choice==5:
        break

    else:
        print("invlid option...!")