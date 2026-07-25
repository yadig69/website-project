# Part 1: Python Basics and Output
# Write a Python script types_and_vars.py that does the following:

# Declares a variable name and assigns it your name as a string.
name = "gregory"
# Declares a variable age and assigns it your age as an integer.
age = 54
inYears  = age + 5
# Declares a variable height and assigns it a floating-point number representing your height in meters.
height = 6.1
# Prints a sentence introducing yourself, for example: "Hello, my name is Alice. I am 20 years old and 1.65 meters tall."
print(f"Hello, my name is {name}. I am {age} years old and {height} meters tall.")
print(f"In 5 years, I will be {inYears} years old.")
# Make sure to use the variables in the print statement (use f-string or string concatenation) instead of hardcoding the values. Run the script to ensure it outputs the correct sentence.

# Modify the script to perform some simple calculations and demonstrate different operators:

# After the introduction sentence, add code that calculates what your age will be in 5 years and print a sentence stating that. For example: "In 5 years, I will be 25 years old."
# Calculate the area of a rectangle with width = 5.5 and height = 2 (you can hardcode these numbers or store them in variables). Print the result in a formatted sentence: "The area of a 5.5 x 2 rectangle is 11.0."

# declaring variables for rectangle dimensions
rectangle_width = 5.5
rectangle_height = 2
# printing the result
print(f"The area of a {rectangle_width} x {rectangle_height} rectangle is {rectangle_width * rectangle_height}.")
# Demonstrate the use of at least two different arithmetic operators (e.g., +, -, *, /, //, or %) and one string concatenation or repetition (e.g., using + to join strings or * to repeat a string).
print("hello \n" * 3)
print(2**3)
print(10//3)
print(10%3)
print(5==5)
print(5!=5)
# Include comments in your code to explain what each section is doing. For example, comment the section where you calculate the age in 5 years and the section where you compute the rectangle area.