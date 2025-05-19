# Making Calculator
import random

try:
     no1=float(input("enter first number :"))
     operator=input("enter your operator like(+,-,*,/): ")
     no2=float(input("enter second number : "))

     if operator=="+":
          print(f"your sum is {no1+no2}")
     elif operator=="-":
          print(f"your sub is {no1-no2}")
     elif operator=="*":
          print(f"your mul is {no1*no2}")
     elif operator=="/":
          print(f"your div is {no1/no2}")
     else:
          print("inalid operators")

     if no1==no2==0:
          print("your first and second no is zeroo..!!!")

except ValueError:
     print("enter valid number")
          
fun_facts = [
    "Did you know calculators used to be the size of a desk?",
    "Python's simplicity makes it great for beginners!",
    "You can build your own AI-powered calculator soon!"
]
print("📚 Fun Fact:", random.choice(fun_facts))

