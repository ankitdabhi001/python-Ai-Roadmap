ab=input("enter your note")

with open("abc.txt","a")as newfile:
    newfile.write(ab)

print("new  text is added")
