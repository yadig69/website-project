import customtkinter as ctk
from datetime import datetime
from todolist import add_task, complete_task, delete_task, list_task, save_tasks

# set appearance and color theme
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class ToDoApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        # window settings
        self.title("To-Do List Manager")
        self.geometry("720x600")

        # internal task list
        self.task_list = []

        # --- Title ---
        ctk.CTkLabel(self, text="Task Manager", font=("Arial", 24, "bold")).pack(pady=10)

        # --- Input Frame ---
        input_frame = ctk.CTkFrame(self)
        input_frame.pack(padx=20, pady=5, fill="x")

        # task title input
        ctk.CTkLabel(input_frame, text="Title:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.title_entry = ctk.CTkEntry(input_frame, width=200)
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)

        # task description input
        ctk.CTkLabel(input_frame, text="Description:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.desc_entry = ctk.CTkEntry(input_frame, width=200)
        self.desc_entry.grid(row=1, column=1, padx=5, pady=5)

        # due date input
        ctk.CTkLabel(input_frame, text="Due Date (YYYY-MM-DD):").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.date_entry = ctk.CTkEntry(input_frame, width=200)
        self.date_entry.grid(row=2, column=1, padx=5, pady=5)

        # --- Buttons ---
        btn_frame = ctk.CTkFrame(self)
        btn_frame.pack(padx=20, pady=5, fill="x")

        ctk.CTkButton(btn_frame, text="Add Task", command=self.handle_add).grid(row=0, column=0, padx=5, pady=5)
        ctk.CTkButton(btn_frame, text="Complete Task", command=self.handle_complete).grid(row=0, column=1, padx=5, pady=5)
        ctk.CTkButton(btn_frame, text="Delete Task", command=self.handle_delete).grid(row=0, column=2, padx=5, pady=5)
        ctk.CTkButton(btn_frame, text="Save Tasks", command=self.handle_save).grid(row=0, column=3, padx=5, pady=5)

        # --- Task Display ---
        ctk.CTkLabel(self, text="Tasks:", font=("Arial", 16)).pack(pady=5)
        self.task_display = ctk.CTkTextbox(self, width=680, height=300)
        self.task_display.pack(padx=20, pady=5)
        # configure green tag for completed tasks
        self.task_display.tag_config("complete", foreground="green")

        # --- Status Label ---
        self.status_label = ctk.CTkLabel(self, text="", text_color="green")
        self.status_label.pack(pady=5)

    def refresh_tasks(self):
        # clear and rewrite the task display box
        self.task_display.delete("1.0", "end")
        if not self.task_list:
            self.task_display.insert("end", "No tasks yet.\n")
        for task in self.task_list:
            status = "✓" if task.completed else "○"
            due_str = task.due_date.strftime("%Y-%m-%d") if task.due_date else "No due date"
            desc_str = f" - {task.description.strip()}" if task.description and task.description.strip() else ""
            line = f"{status} {task.title} (Due: {due_str}){desc_str}\n"
            # insert completed tasks in green, others in default color
            if task.completed:
                self.task_display.insert("end", line, "complete")
            else:
                self.task_display.insert("end", line)

    def set_status(self, message, color="green"):
        # update the status label with a message
        self.status_label.configure(text=message, text_color=color)

    def handle_add(self):
        # get values from input fields
        title = self.title_entry.get().strip()
        description = self.desc_entry.get().strip()
        due_date_str = self.date_entry.get().strip()

        if not title:
            self.set_status("Title is required.", "red")
            return

        # parse due date if provided
        due_date = None
        if due_date_str:
            try:
                due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
            except ValueError:
                self.set_status("Invalid date format. Use YYYY-MM-DD.", "red")
                return

        add_task(self.task_list, title, description, due_date)
        self.set_status(f"Task '{title}' added!")
        # clear input fields after adding
        self.title_entry.delete(0, "end")
        self.desc_entry.delete(0, "end")
        self.date_entry.delete(0, "end")
        self.refresh_tasks()

    def handle_complete(self):
        # mark the task matching the title as complete
        title = self.title_entry.get().strip()
        if not title:
            self.set_status("Enter a task title to complete.", "red")
            return
        complete_task(self.task_list, title)
        self.set_status(f"Task '{title}' marked as complete!", "green")
        self.refresh_tasks()

    def handle_delete(self):
        # delete the task matching the title
        title = self.title_entry.get().strip()
        if not title:
            self.set_status("Enter a task title to delete.", "red")
            return
        delete_task(self.task_list, title)
        self.set_status(f"Task '{title}' deleted!")
        self.refresh_tasks()

    def handle_save(self):
        # save all tasks to tasks.csv
        save_tasks(self.task_list)
        self.set_status("Tasks saved to tasks.csv!")


# entry point — runs the GUI when the file is executed directly
if __name__ == "__main__":
    app = ToDoApp()
    app.mainloop()
