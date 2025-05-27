# check the user name

register_users=set()

def user(username):
    clean=username.strip().lower()

    if clean in register_users:
        print(f"username {username} is alredy taken.")
    else:
        register_users.add(clean)
        print(f"welcome {username}")

while True:

    a=input("enter user name = ")
    if a.lower() == "exit":
        break
    user(a)
print(f"register user is : {register_users}")