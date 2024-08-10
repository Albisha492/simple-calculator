#case no: 1
def add(a , b):
    return a+b
#case no:2
def subtract(a,b):
    return a-b
#case no:3
def multiply (a,b):
    return a * b
#case no:4
def divide (a,b):
  if b==0:
      return "error:division by zero"
  return a/b

import streamlit as st

st.title("Simple Calculator")

num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")

operation = st.selectbox("Choose an operation", ("Add", "Subtract", "Multiply", "Divide"))

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
            result = "Error! Division by zero."

    st.write(f"The result is: {result}")
