import streamlit as st

st.set_page_config(page_title="Calculator Builder", layout="wide")
# App Title
st.title("🧮 Agentic Calculator")

# Create two columns
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("First Number", value=0.0)

with col2:
    num2 = st.number_input("Second Number", value=0.0)

# Operation selection
operation = st.selectbox(
    "Operation",
    ["Add", "Subtract", "Multiply", "Divide"]
)

# Calculate button
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 == 0:
            st.error("Cannot divide by zero!")
        else:
            result = num1 / num2

    if not (operation == "Divide" and num2 == 0):
        st.success(f"Result: {result}")
