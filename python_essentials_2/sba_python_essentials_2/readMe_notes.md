# Personal todo-list manager

## ## Overview and Objectives

In this project you will design and implement a Personal To-Do List Manager that integrates various Python concepts learned throughout the course, including modules, file handling, and object-oriented programming. You will:

* Create a **Task** class to represent individual to-do items.
* Develop functions (or methods) for adding, completing, deleting, and listing tasks.
* Build a text-based user interface that enables interactive management of tasks.
* Implement data persistence by saving tasks to and loading them from a file.
* (Optional) Enhance your program with an external package for improved output formatting or additional features.

By the end of this project, you will have a fully functional console application that allows users to manage their daily tasks effectively.

### Task 1: Define the Task Class

* **Create a new module** (e.g., `task.py`) and define a class `Task` with the following:
  * **Attributes:**
    * `title`: A short description of the task.
    * `due_date`: An optional due date (as a `datetime.date` object or a string).
    * `completed`: A boolean status indicating whether the task is complete.
  * **Initializer:**
    * `__init__(self, title, due_date=None, completed=False)` to set up the attributes.
  * **Methods:**
    * `__str__(self)`: Returns a well-formatted string representation of the task, e.g., `"[-] Submit assignment (due 2025-03-10)"`, where `[X]` indicates a completed task.

### Task 2: Implement To-Do Manager Functions

* **Create a new module** (e.g., `todolist.py`) that includes functions to manage tasks:
  * `add_task(task_list, title, due_date=None)`: Creates a new `Task` and adds it to the list. If `due_date` is provided as a string, parse it into a `datetime.date` (assume format “YYYY-MM-DD”). Use exception handling to catch parsing s.b.a errors and inform the user.
  * `complete_task(task_list, index)`: Marks the task at the given index as completed. If the index is invalid, handle the error gracefully.
  * `delete_task(task_list, index)`: Removes the task at the given index. Include error handling for invalid indices.
  * `list_tasks(task_list)`: Returns or prints a formatted list of tasks showing index, status, title, and due date. Indicate if a task is overdue by comparing the due date with today’s date.

### Task 3: Develop the User Interface

* **Create a main script** (e.g., `main.py`) that:
  * Presents a text-based menu with the options:
    * **(A)** Add a new task.
    * **(C)** Mark a task as completed.
    * **(D)** Delete a task.
    * **(L)** List all tasks.
    * **(Q)** Quit.
  * Implements the menu loop so that after each operation the menu is shown again until the user chooses to quit.
  * For each menu option, prompts the user for necessary input and calls the corresponding function from `todolist.py`.
  * Before quitting, prompts the user to save the current task list to a file.

### Task 4: Data Persistence

* **Enhance your program** to save tasks to a file (e.g., `tasks.txt` or `tasks.csv`) and load them on startup:
  * When the program starts, check if the file exists using the `os` module. If it exists, load the tasks and reconstruct the `Task` objects.
  * When the user chooses to save (or upon exiting), write the tasks to the file in a structured format (e.g., comma-separated values).
  * Use try/except blocks to handle potential file I/O errors, providing user-friendly error messages.

### (Optional) Task 5: External Package Enhancement

* **Optionally** , use a third-party package (such as `colorama` or `prettytable`) to enhance the user interface:
* For example, color-code overdue tasks or format the task list as a table.
* Include a comment at the top of your code explaining how to install the package (e.g., `# Requires colorama; install with: pip install colorama`).
