import math
# Create a new Python file named utilities.py that defines at least the following functions:
# greet(name): Returns a greeting string for the given name.

def greet(name: str) -> str:
    return f"Hello, {name}! Welcome to Python Essentials."

# factorial(n): Returns the factorial of n (you may use functions from the math module if needed).

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return math.factorial(n)

"""
 This is a sample Python script.
"""