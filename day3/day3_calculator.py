import streamlit as st
import math

# --- Page Config ---
st.set_page_config(page_title="AI SmartCalc", page_icon="🧠")
st.title("🧠 AI SmartCalc v3.0")
st.caption("Smart Calculator with Memory, History & Expression Parsing")

# --- Session State Setup ---
def initialize_state():
    if "history" not in st.session_state:
        st.session_state.history = []
    if "memory" not in st.session_state:
        st.session_state.memory = None

# --- Calculation Logic ---
def basic_calculator(num1, num2, op):
    if op == "➕":
        result = num1 + num2
        expression = f"{num1} + {num2} = {result}"
    elif op == "➖":
        result = num1 - num2
        expression = f"{num1} - {num2} = {result}"
    elif op == "✖":
        result = num1 * num2
        expression = f"{num1} × {num2} = {result}"
    elif op == "➗":
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result = num1 / num2
        expression = f"{num1} ÷ {num2} = {result}"
    return result, expression

def parse_expression(expression):
    result = eval(expression)
    return result, f"{expression} = {result}"

def handle_calculation(mode, num1=None, num2=None, op=None, expression=None):
    if mode == "📐 Basic Inputs":
        return basic_calculator(num1, num2, op)
    else:
        return parse_expression(expression)

def display_result(result, expression):
    st.success(f"✅ {expression}")
    st.session_state.history.append(expression)
    st.session_state.memory = result

def clear_data(history=False, memory=False):
    if history:
        st.session_state.history = []
        st.success("✅ History cleared!")
    if memory:
        st.session_state.memory = None
        st.success("✅ Memory cleared!")

def show_memory():
    if st.session_state.memory is not None:
        st.info(f"🧠 Memory: Last result = `{st.session_state.memory}`")

def show_history():
    st.subheader("📜 History (Last 5)")
    if st.session_state.history:
        for i, entry in enumerate(reversed(st.session_state.history[-5:]), 1):
            st.write(f"{i}. {entry}")
    else:
        st.write("No history yet.")

# --- App Logic ---
def main():
    initialize_state()

    # Input selection
    calc_mode = st.radio("🧩 Choose mode", ["📐 Basic Inputs", "🧮 Expression Parsing"])

    if calc_mode == "📐 Basic Inputs":
        num1 = st.number_input("Enter first number", value=0.0)
        op = st.selectbox("Choose operation", ["➕", "➖", "✖", "➗"])
        num2 = st.number_input("Enter second number", value=0.0)
    else:
        expression = st.text_input("Enter expression (e.g. 5 + 3 * 2):", value="")

    # Buttons
    col1, col2, col3 = st.columns(3)
    calc_clicked = col1.button("🧠 Calculate")
    clear_history = col2.button("🧹 Clear History")
    clear_memory = col3.button("🗑️ Clear Memory")

    # Clear actions
    if clear_history:
        clear_data(history=True)
    if clear_memory:
        clear_data(memory=True)

    # On Calculate
    if calc_clicked:
        try:
            if calc_mode == "📐 Basic Inputs":
                result, expression_str = handle_calculation(calc_mode, num1=num1, num2=num2, op=op)
            else:
                result, expression_str = handle_calculation(calc_mode, expression=expression)
            display_result(result, expression_str)
        except Exception as e:
            st.error(f"❌ Error: {e}")
            st.session_state.history.append(f"❌ Error: {e}")

    # Output Sections
    st.markdown("---")
    show_memory()
    show_history()
    st.markdown("---")
    st.caption("🚀 Tip: You can extend this with permanent file/database saving.")

# Run the app
main()
