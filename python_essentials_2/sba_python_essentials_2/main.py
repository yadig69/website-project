# import colorama for colored terminal output
import colorama
from colorama import Fore, Back, Style

# import date utilities for parsing and comparing due dates
from datetime import datetime, date

# import task management functions from todolist module
from todolist import add_task, complete_task, delete_task, list_task, save_tasks

def To_Do_List():
    # initialize an empty list to store tasks
    Task = []

    # keep the menu running until the user chooses to quit
    while True:
        # display the menu options
        print("\nOptions:")
        print("1. Add task")
        print("2. Mark task as complete")
        print("3. Delete task")
        print("4. List tasks")
        print("5. Quit")

        # get the user's menu selection
        choice = input("Enter your choice(1 - 4): ").strip()

        if choice == "1":
            # prompt for task title and optional due date
            title = input("Enter task title: ")
            due_date = input("Enter due date (YYYY-MM-DD) or press Enter to skip: ")
            if due_date:
                # parse the due date string into a datetime object
                due_date = datetime.strptime(due_date, "%Y-%m-%d")
            else:
                # no due date provided
                due_date = None
            # add the new task to the list
            add_task(Task, title, due_date)

        elif choice == "2":
            # prompt for the task title and mark it as complete
            title = input("Enter task title to mark as complete: ")
            complete_task(Task, title)

        elif choice == "3":
            # prompt for the task title and remove it from the list
            title = input("Enter task title to delete: ")
            delete_task(Task, title)

        elif choice == "4":
            # display all current tasks
            list_task(Task)

        elif choice == "5":
            # prompt the user to save tasks before quitting
            save = input("Would you like to save your tasks before quitting? (y/n): ").strip().lower()
            if save == "y":
                save_tasks(Task)
            print("Goodbye!")
            break

        else:
            # handle any invalid menu input
            print("Invalid choice. Please try again.")

# entry point — runs the program when the file is executed directly
if __name__ == "__main__":
    To_Do_List()
