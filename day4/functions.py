# Function-based Smart Calculator

def calculate(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "❌ Error: Division by zero!"
    else:
        return "⚠️ Invalid operation."

# Call the function
n1 = float(input("Enter number 1: "))
n2 = float(input("Enter number 2: "))
operator = input("Choose operation (+ - * /): ")

result = calculate(n1, n2, operator)
print("Result:", result)
