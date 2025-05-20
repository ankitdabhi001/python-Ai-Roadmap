# smart calculator

import random

def calculator(no1,no2,op):
    if op=="+":
        return no1+no2
    elif op=="-":
        return no1-no2
    elif op=="*":
        return no1*no2
    elif op=="/":
        return no1/no2
    else:
        return "invalid operator"
    
n1=float(input("enter first number : "))
n2=float(input("enter second number : "))
operator=input("enter operator like:-  +,-,*,/ : ")

result=calculator(n1,n2,operator)
print(f"your answer is {result}")

import random

def tell_joke():
    jokes = [
        "😄 Why don't scientists trust atoms? Because they make up everything!",
        "😂 Why did the computer go to the doctor? Because it had a virus!",
        "🤣 Why do Python developers wear glasses? Because they can't C!",
        "😆 What do you call 8 hobbits? A hobbyte!",
        "😁 Why was the math book sad? It had too many problems!"
    ]

    joke = random.choice(jokes)
    print("Here's a random joke for you:")
    print(joke)

# Call the function
tell_joke()
