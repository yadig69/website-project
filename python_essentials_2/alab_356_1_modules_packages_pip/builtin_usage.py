# Imports the math, random, and platform modules.
import math
import random
import platform
# Generates a random integer between 1 and 100 using the random module.
random_number = random.randint(1, 100)
print(f"Random Number = {random_number}")
# Calculates the square root of that number using math.sqrt and rounds it down (using math.floor or by converting to an integer).
sqrt_value = math.sqrt(random_number)
rounded_sqrt = math.floor(sqrt_value)
print(f"Square Root (floored) = {rounded_sqrt}")
# Retrieves and prints the system’s OS name and Python version using functions from the platform module.
os_name = platform.system()
python_version = platform.python_version()
# print the system information
print(f"Operating System: {os_name}")
print(f"Python Version: {python_version}")