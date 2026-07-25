# Write a Python script simple_calculator.py that:
print("-- simple calculator --")
# Asks the user to input two numbers (use two separate input() calls). Make sure to convert these inputs from strings to integers or floats as needed.
number_one = float(input("Enter the first number: "))
number_two = float(input("Enter the second number: "))
# Asks the user to choose an operation (e.g., addition, subtraction, multiplication, division). This can be a simple prompt like "Choose an operation (+, -, *, /): ".
operation = input("Choose an operation (+, -, *, /): ")
# Performs the chosen operation on the two numbers.
if operation == "+":
    result = number_one + number_two
    print(f"{number_one} + {number_two} = {result}")
    print("Thank you for using the calculator!")
elif operation == "-":
    result = number_one - number_two
    print(f"{number_one} - {number_two} = {result}")
    print("Thank you for using the calculator!")
elif operation == "*":
     result = number_one * number_two
     print(f"{number_one} * {number_two} = {result}")
     print("Thank you for using the calculator!")
elif operation == "/":
    if number_two == 0:
        print("Error: Division by zero is not allowed.")
        result = number_one / number_two
        print(f"{number_one} / {number_two} = {result}")
        print("Thank you for using the calculator!")
        exit()
else:
    print("Error: Invalid operation. Please choose +, -, *, or /.")
# Prints the result in a user-friendly way. For example: "7 * 3 = 21" (assuming the user chose 7, 3, and *).
# Ensure the program can handle basic invalid inputs gracefully. For instance, if the user enters a non-numeric value for the numbers or an unsupported operation symbol, print an error message. (Tip: You can use an if-elif-else structure to check the operation and a simple if to validate numeric input using isdigit() or exception handling which will be covered later. For now, focus on the structure and assume valid input for simplicity if exception handling is not yet learned.)


# display the formatted calculation result,using :g cleans up trailing zeros and decimal points```python

print(f"\nResult: {number_one:g} {operation} {number_two:g} = {result:g}")
