# Write a script basic_functions.py that defines and uses simple functions:
print("-- basic functions --")

# Define a function greet_user() that takes a name (string) as a parameter and prints a greeting, e.g., "Hello, <name>! Welcome!". If no name is provided (you can simulate this by calling greet_user() with an empty string or by using a default parameter value), it should print "Hello! Welcome!".
def greet_user(name=""):
    if name:
        print(f"Hello, {name}! Welcome!")
    else:
        print("Hello! Welcome!")
print(greet_user(input("what is your name? ")))
# called with a sample name
greet_user("Greg")
# called without a name — uses default
greet_user()
# Define a function add_two_numbers(a, b) that returns the sum of two numbers a and b.
def add_two_numbers(a, b):
    return a + b
print(add_two_numbers(4, 54))
# Define a function is_even(num) that returns True if num is even or False otherwise.
def is_even(num):
    return num % 2 == 0

num = int(input("please enter a number "))
results = is_even(num)
print(f"{num} is even: {results}")
# In the main part of the script (outside the functions), demonstrate each function:
# Call greet_user() with a sample name and without a name.
# Call add_two_numbers() with two numbers, print the result.
# Call is_even() on a couple of numbers (one even, one odd) and print the results in a descriptive way (e.g., "4 is even: True").
# Include comments explaining what each function is intended to do. Use appropriate return statements for functions 2 and 3, and show that the returned values can be stored in variables or used in expressions.