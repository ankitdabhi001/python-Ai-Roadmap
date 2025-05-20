# use the some basic function in this assistant
import random

def math_assistance():

    print("1. Add two numbers")
    print("2. Subtract two numbers")
    print("3. Convert Celsius to Fahrenheit")
    print("4. Calculate BMI")
    print("5. Get a Math Tip")

    choice=int(input("enter youe choice like (1,2,3,4,5) = "))

    if choice==1:
        a=int(input("enter first number :"))
        b=int(input("enter second number : "))
        print(f"your addition is {a+b}")

    elif choice==2:
        a=int(input("enter first number :"))
        b=int(input("enter second number : "))
        print(f"your substraction is {a-b}")

    elif choice==3:
        celsius=float(input("enter celsious : "))
        print(f"fahrenheit is :{(celsius * 9/5) + 32}°F") 

    elif choice==4:
        height=int(input("enter your height in cm : "))
        hc=height/100
        weight=int(input("enter your weight in kg : "))
        bmi= weight/(hc ** 2)
        print(f"your BMI  is : {bmi:.2f}")

    elif choice ==5:
        tips = [
            "🔢 Tip: Multiplying by 5 is the same as multiplying by 10 and then dividing by 2!",
            "📐 Tip: Area of a triangle is 1/2 × base × height.",
            "🧠 Tip: The order of operations is PEMDAS (Parentheses, Exponents, Multiply/Divide, Add/Subtract)."
        ]
        print(random.choice(tips))

    else:
        print("❌ Invalid choice. Try again.")

math_assistance()