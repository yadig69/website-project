# Create a script data_processing.py that simulates a simple data processing scenario:
print("-- data processing --")
# Define a function get_average_grade(grades_tuple) that takes a tuple of numeric grades and returns the average. Include a try/except to handle the case if the tuple is empty (to avoid division by zero), returning None or printing a warning in that case.
def get_average_grade(grades_tuple):
    try:
        if not grades_tuple:
            raise ValueError("Cannot calculate average of an empty tuple.")
        return sum(grades_tuple) / len(grades_tuple)
    except ValueError as e:
        print(f"Error: {e}")
        return None
# Define a dictionary course_grades where keys are course names (e.g., “Math”, “Science”, “History”) and values are tuples of grades.
course_grades = {
    "MERN": (90, 85, 92, 88),
    "PYTHON": (95, 87, 91, 89),
    "History": (),
    "AWS_Cloud": (88, 92, 85, 90),
    "Cloud_Infrastructure": (92, 89, 94, 91)
}
# Use a loop to iterate over course_grades. For each course, call get_average_grade(grades_tuple) and print a message like: "The average grade for Math is 85.2". Handle any None values or exceptions gracefully.
for course, grades in course_grades.items():
    average = get_average_grade(grades)
    if average is not None:
        print(f"The average grade for {course} is {average:.1f}")
    else:
        print(f"No grades available for {course}")
# Intentionally include an edge case, such as one course having an empty tuple of grades, to demonstrate your exception handling works.