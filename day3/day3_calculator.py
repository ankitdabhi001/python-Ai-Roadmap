
#streamlit run "E:/Python Roadmap/python-Ai-Roadmap/day3/day3_calculator.py"
import streamlit as st
import math

# --- Set up the page ---
st.set_page_config(page_title="AI SmartCalc", page_icon="🧠")
st.title("🧠 AI SmartCalc v3.0")
st.caption("Smart Calculator with Memory, History & Expression Parsing")

# --- Session State Initialization ---
if "history" not in st.session_state:
    st.session_state.history = []

if "memory" not in st.session_state:
    st.session_state.memory = None

# --- Input Options ---
calc_mode = st.radio("🧩 Choose mode", ["📐 Basic Inputs", "🧮 Expression Parsing"])

if calc_mode == "📐 Basic Inputs":
    num1 = st.number_input("Enter first number", value=0.0)
    op = st.selectbox("Choose operation", ["➕", "➖", "✖", "➗"])
    num2 = st.number_input("Enter second number", value=0.0)
else:
    expression = st.text_input("Enter expression (e.g. 5 + 3 * 2):", value="")

# --- Buttons ---
col1, col2, col3 = st.columns(3)
calc_clicked = col1.button("🧠 Calculate")
clear_history = col2.button("🧹 Clear History")
clear_memory = col3.button("🗑️ Clear Memory")

# --- Clear Actions ---
if clear_history:
    st.session_state.history = []
    st.success("✅ History cleared!")

if clear_memory:
    st.session_state.memory = None
    st.success("✅ Memory cleared!")

# --- Calculation Logic ---
if calc_clicked:
    try:
        if calc_mode == "📐 Basic Inputs":
            if op == "➕":
                result = num1 + num2
                expression_str = f"{num1} + {num2} = {result}"
            elif op == "➖":
                result = num1 - num2
                expression_str = f"{num1} - {num2} = {result}"
            elif op == "✖":
                result = num1 * num2
                expression_str = f"{num1} × {num2} = {result}"
            elif op == "➗":
                if num2 == 0:
                    raise ZeroDivisionError("Cannot divide by zero")
                result = num1 / num2
                expression_str = f"{num1} ÷ {num2} = {result}"

        else:
            result = eval(expression)
            expression_str = f"{expression} = {result}"

        # Store in history and memory
        st.success(f"✅ {expression_str}")
        st.session_state.history.append(expression_str)
        st.session_state.memory = result

    except Exception as e:
        st.error(f"❌ Error: {e}")
        st.session_state.history.append(f"❌ Error: {e}")

# --- Show Memory ---
st.markdown("---")
if st.session_state.memory is not None:
    st.info(f"🧠 Memory: Last result = `{st.session_state.memory}`")

# --- Show History ---
st.subheader("📜 History (Last 5)")
if st.session_state.history:
    for i, entry in enumerate(reversed(st.session_state.history[-5:]), 1):
        st.write(f"{i}. {entry}")
else:
    st.write("No history yet.")

# --- Footer ---
st.markdown("---")
st.caption("🚀 Tip: You can extend this with permanent file/database saving.")
