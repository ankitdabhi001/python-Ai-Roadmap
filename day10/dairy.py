from datetime import datetime


def dairy_entry():
    time=datetime.now().strftime("%d-%m-%y %H:%M:%S")
    final_entry=f"{time}\n {entry}\n"

    with open("dairyy.txt","a") as file:
        file.write(final_entry)

while True:
        
    entry=input("enter your today entry : ")
    if entry.lower() == "exit":
        break


dairy_entry()