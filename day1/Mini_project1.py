#create greet chatboat

import random

name=input("what is your name : ")
age=int(input("what is your current age : "))
ans=input("i speak you one joke you listen give me answer in like 'yes/no' : ")


print(f"hii {name}!")
print(f"Your Current age is {age}")
print(f"your answer is {ans}")

if age<18:
    print(f"you are Teenager because your age is {age}")
elif age<=30 or age>=18:
    print(f"you are very yong because your age is {age}")





jokes=[
    "this is joke1",
     "this is joke2",
      "this is joke3",
]

ans=ans.lower()

if ans.lower()=="yes":
    print(random.choice(jokes))

elif ans.lower()=="no":
    print("thank you")

else:
    print("choose only yes or no")