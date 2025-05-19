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


if no1==no2==0:
     print("your number is zeroo..!!!")