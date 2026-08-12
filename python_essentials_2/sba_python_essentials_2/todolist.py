from datetime import date, datetime
from sba_task_manager import Task



def add_task(task_list: list, title_id: str, due_date: datetime = None):
    """Add a task to the task list."""
   # task_list.append(Task(title, due_date))
    parsed_date = due_date
    
    if isinstance(due_date, str):
     try:
        parsed_date = datetime.strptime(due_date, "%Y-%m-%d").date()
        
     except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

            return

    new_task = Task(title_id, parsed_date)
    task_list.append(new_task)
    print(f"Task '{title_id}' added successfully!")
    
def complete_task(task_list: list, title_id: str):
    """Mark a task as complete."""
    for task in task_list:
        if task.title == title_id:
            task.completed = True
            print(f"Task '{title_id}' marked as complete!")
            return
    print(f"Task '{title_id}' not found.")