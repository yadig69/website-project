from datetime import datetime
from typing import Optional, Union
from colorama import Fore, Back, Style



class Task:
    """A task in the task manager."""
    def __init__(self, title_id: str, due_date: Optional[datetime] = None, description = " ", completed = False):
        
        self.title = title_id
        self.due_date = due_date
        self.description = description
        self.completed = completed
    
    def __str__(self):
        status = "[X]" if self.completed else "-"
        due_str = f" (due {self.due_date})" if self.due_date else ""
        return f"{status} {self.title}{due_str}"
