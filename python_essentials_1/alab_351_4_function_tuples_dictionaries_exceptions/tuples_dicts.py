# Write a script tuples_dicts.py that:
print("-- tuples and dictionaries --")
# Creates a tuple months containing the names of the twelve months.
months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
print(months)
# Prints the first and last month from the tuple (index 0 and index -1).
print(months[0], months[-1])
# Attempts to modify the tuple (e.g., months[0] = "NewMonth") inside a try/except block to demonstrate that tuples are immutable. Catch the exception and print a message like: "Tuples are immutable, error: <error_message>".
try:
    months[0] = "NewMonth"
    print("This won't be printed because the above line raises TypeError")
except TypeError as e:
        print(f"Tuples are immutable, error: {e}")
# Creates a dictionary students where keys are student names and values are their grades (choose 3-5 sample name-grade pairs).
students = {"Alice": 90, "Bob": 85, "Charlie": 92, "Diana": 88}
print(students)
# Adds a new student and grade to the dictionary, then prints all student names and grades.
students["Eve"] = 95
print(students)
# Updates one of the existing student’s grades, then prints the updated entry.
students["Bob"] = 87
# Uses a loop to print out each student’s name and grade in a formatted way, e.g., "Alice: 90".
for name, grade in students.items():
    print(f"{name}: {grade}")

