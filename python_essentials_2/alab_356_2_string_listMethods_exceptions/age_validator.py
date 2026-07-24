# Task 3: Custom Exception Test (Age Validator)
# Write a function validate_age(age) that:
# Accepts a parameter age.
def validate_age(age):
# Raises a ValueError with an appropriate message if the age is not between 0 and 120 (inclusive).
    if not (0 <= age <= 120):
        raise ValueError("Age must be between 0 and 120.")
# Write a short script (e.g., age_validator.py) that:
if __name__ == "__main__":
    try:
        user_input = int(input("Enter your age: "))
        validate_age(user_input)
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print("Age is valid and accepted.")
# Prompts the user to enter their age.
# Calls validate_age with the input value.
# Uses try/except to catch the exception if the age is invalid, printing the error message.
# If no exception is raised, prints a message indicating that the age is accepted.
