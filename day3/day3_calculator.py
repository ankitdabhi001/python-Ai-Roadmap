import streamlit as st
#streamlit run "E:/Python Roadmap/python-Ai-Roadmap/day3/day3_calculator.py"

# Page config
st.set_page_config(page_title="AI SmartCalc", page_icon="🧮")

# Title
st.title("🧮 AI SmartCalc with History")
st.markdown("A web-based smart calculator built with Streamlit and Python.")

# Initialize session state for history
if "history" not in st.session_state:
    st.session_state.history = []

# Input section
num1 = st.number_input("🔢 Enter first number", value=0.0, step=0.1)
num2 = st.number_input("🔢 Enter second number", value=0.0, step=0.1)
operation = st.selectbox("📌 Choose an operation", ["➕ Add", "➖ Subtract", "✖ Multiply", "➗ Divide"])

# Calculate on button click
if st.button("🧠 Calculate"):
    try:
        if operation == "➕ Add":
            result = num1 + num2
            expression = f"{num1} + {num2} = {result}"
        elif operation == "➖ Subtract":
            result = num1 - num2
            expression = f"{num1} - {num2} = {result}"
        elif operation == "✖ Multiply":
            result = num1 * num2
            expression = f"{num1} × {num2} = {result}"
        elif operation == "➗ Divide":
            if num2 != 0:
                result = num1 / num2
                expression = f"{num1} ÷ {num2} = {result}"
            else:
                expression = "❌ Error: Cannot divide by zero!"
                st.error(expression)
                st.session_state.history.append(expression)
                st.stop()
        
        # Display result and store in history
        st.success(f"✅ {expression}")
        st.session_state.history.append(expression)
    except Exception as e:
        error_msg = f"⚠️ Error: {e}"
        st.error(error_msg)
        st.session_state.history.append(error_msg)

# History display
st.markdown("---")
st.subheader("🕘 Calculation History")
if st.session_state.history:
    for i, item in enumerate(reversed(st.session_state.history[-5:]), 1):
        st.write(f"{i}. {item}")
else:
    st.write("No calculations yet.")

# Fun fact
st.markdown("---")
st.info("💡 Fun Fact: You’re building a memory-powered calculator like real digital machines!")

# Footer
st.caption("🚀 Tip: You can extend this history to save to file or database for full persistence.")
