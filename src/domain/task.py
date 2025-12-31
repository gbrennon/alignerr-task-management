from datetime import date
from src.domain.errors import TaskWasAlreadyDoneError


class Task:
    def __init__(self, title: str, description: str, due_date: date):
        self.title = title
        self.description = description
        self.done = False
        self.due_date = due_date

    def mark_as_done(self) -> None:
        if self.done:
            raise TaskWasAlreadyDoneError("Task is already marked as done")
        self.done = True
