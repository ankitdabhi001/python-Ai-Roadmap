# write simple note and read in file


# write in file :
a=input("enter your note : ")


with open("practice.txt","a") as file:
    file.write(a + "\n")

# read file:

with open("practice.txt","r") as file:
    print(file.read())