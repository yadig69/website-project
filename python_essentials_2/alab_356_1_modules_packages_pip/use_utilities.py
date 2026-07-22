from mypackage import utilities

# ask for the user's name
user_name = input("Enter your name: ")

# generate and print the greeting
welcome_message = utilities.greet(user_name)
print(welcome_message)

# call factorial function and print output
try:
    num = int(input("Enter a number to find its factorial: "))
    print(f"The factorial of {num} is: {utilities.factorial(num)}")
except ValueError as e:
    print(f"Error: {e}")
    
    
    ##########
    
import math

result = math.e != math.pow(2, 4)
print(int(result))

