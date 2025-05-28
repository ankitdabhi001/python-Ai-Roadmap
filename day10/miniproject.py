# Take multiple notes from user
# Save to notes.txt
# Show all previous notes on startup
import os 

if os.path.exists("notes.txt"):

    with open("notes.txt","r") as file:
        print("your old notes is here :")
        print(file.read())

while True:
    a=input("enter your notes : ")
    if a.lower()=="exit":
        break

    with open("notes.txt","a") as file:
        file.write(a + "\n")

