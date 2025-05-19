#create greet chatboat

name=input("what is your name : ")
age=int(input("what is your current age : "))

print(f"hii{name}!")
print(f"Your Current age is {age}")

if age<18:
    print(f"you are Teenager because your age is {age}")
elif age<=30 or age>=18:
    print(f"you are very yong because your age is {age}")


