import streamlit as st

st.title("🧮 Simple Web Calculator")

# Input fields
num1 = st.number_input("Enter first number:", step=1.0)
num2 = st.number_input("Enter second number:", step=1.0)

# Operation selection
operation = st.radio("Choose an operation:", ("Add", "Subtract", "Multiply", "Divide"))

# Calculate when button is clicked
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero!"
    
    st.success(f"Result: {result}")
