# import date and datetime for due date parsing and comparison
from datetime import date, datetime

# import the Task class to create new task objects
from sba_task_manager import Task


def add_task(task_list: list, title_id: str, due_date: datetime = None):
    """Add a task to the task list."""
    # start with the due_date as-is
    parsed_date = due_date

    # if due_date was passed as a string, convert it to a date object
    if isinstance(due_date, str):
        try:
            parsed_date = datetime.strptime(due_date, "%Y-%m-%d").date()
        except ValueError:
            # if the format is wrong, notify the user and stop
            print("Invalid date format. Please use YYYY-MM-DD.")
            return

    # create a new Task object with the title and parsed date
    new_task = Task(title_id, parsed_date)
    # append the new task to the task list
    task_list.append(new_task)
    print(f"Task '{title_id}' added successfully!")


def complete_task(task_list: list, title_id: str):
    """Mark a task as complete."""
    # loop through the list to find the task by title
    for task in task_list:
        if task.title == title_id:
            # set completed to True and exit the function
            task.completed = True
            print(f"Task '{title_id}' marked as complete!")
            return
    # if no matching task was found, notify the user
    print(f"Task '{title_id}' not found.")


def delete_task(task_list: list, title_id: str):
    """Delete a task from the task list."""
    # loop through the list using index to find the task by title
    for i, task in enumerate(task_list):
        if task.title == title_id:
            # remove the task at the found index and exit
            del task_list[i]
            print(f"Task '{title_id}' deleted successfully!")
            return
    # if no matching task was found, notify the user
    print(f"Task '{title_id}' not found.")


def save_tasks(task_list: list, filename: str = "tasks.csv"):
    """Save all tasks to a CSV file."""
    try:
        # open the file in write mode
        with open(filename, "w") as f:
            for task in task_list:
                # format due_date as a string or leave empty if none
                due_date_str = task.due_date.strftime("%Y-%m-%d") if task.due_date else ""
                # write each task as a comma-separated line
                f.write(f"{task.title},{due_date_str},{task.completed}\n")
        print(f"Tasks saved to {filename}")
    except IOError as e:
        # handle any file writing errors
        print(f"Error saving tasks: {e}")


def list_task(task_list):
    """Display all tasks in the list."""
    # if the list is empty, notify the user
    if not task_list:
        print("No tasks in the list.")
    else:
        print("Tasks:")
        for task in task_list:
            # show ✓ for completed tasks and ○ for incomplete
            status = "✓" if task.completed else "○"
            # format due date or show placeholder if none
            due_date_str = task.due_date.strftime("%Y-%m-%d") if task.due_date else "No due date"
            print(f"{status} {task.title} (Due: {due_date_str})")
