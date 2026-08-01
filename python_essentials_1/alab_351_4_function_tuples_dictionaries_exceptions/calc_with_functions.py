# Create a script calc_with_functions.py that refactors the calculator from Module 2 (Task 2.3) using functions:
print("-- calculator with functions --")

# Write separate functions for each operation: add(a,b), subtract(a,b), multiply(a,b), divide(a,b) – each returning the result.
def add(a,b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
# Write a calculate(a, b, op) function that takes two numbers and a symbol for operation, and uses if/elif to call the correct operation function. It should handle an invalid operation by returning or printing an error message.
def calculate(a, b, op):
    if op == "+":
        return add(a, b)
    elif op == "-":
        return subtract(a, b)
    elif op == "*":
        return multiply(a, b)
    elif op == "/":
        return divide(a, b)
    else:
        raise ValueError("Invalid operation. Please use +, -, *, or /.")
# In the main program, ask the user for two numbers and an operation (just like before), but now use the calculate function to get the result and print it.
try:
    a = float(input("Enter the first number: "))
    op = input("Enter the operation (+, -, *, /): ")
    b = float(input("Enter the second number: "))
    result = calculate(a, b, op)
    print(f"{a} {op} {b} = {result}")

except ValueError as e:
    print(f"Error: {e}")
# Add exception handling to gracefully handle errors such as division by zero or invalid numeric input. Use try/except around the input conversion and the division operation at minimum.

# This task will demonstrate functions calling other functions and basic exception handling.