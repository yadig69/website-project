# Write a script exception_demo.py that contains the following:
print("-- exceptions --")

# ? 1: A function safe_divide(a, b) that returns the result of a / b if b is not zero. If b is zero, the function should raise a ValueError with a message like “Cannot divide by zero”.
def safe_divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by 0")
    return a / b
# Use a try/except structure to call safe_divide with some test values that include a zero divisor. Catch the ValueError and print an error message to the user.
try:
    result = safe_divide(10, 0)
    print(result)
    print("Division operation completed")
except ValueError as e:
    print(f"Error: {e}")


# Include a finally clause in the try/except that prints a message like “Division operation completed” whether or not an error occurred.
finally:
    print("Division operation completed")
# Also demonstrate catching a generic exception by performing an unsafe operation (for example, converting an invalid string to int in a try block) and catching the generic Exception to print a message.
    print(int("hello"))
# This will showcase your understanding of raising and catching exceptions.