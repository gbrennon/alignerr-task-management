from datetime import date
import pytest
from src.domain.task import Task
from src.domain.errors import TaskWasAlreadyDoneError


def test_task_initialization():
    task = Task("Buy groceries", "Need to buy milk, eggs, and bread", date(2025, 12, 31))
    assert task.title == "Buy groceries"
    assert task.description == "Need to buy milk, eggs, and bread"
    assert task.done is False
    assert task.due_date == date(2025, 12, 31)


def test_mark_as_done():
    task = Task("Buy groceries", "Need to buy milk, eggs, and bread", date(2025, 12, 31))
    task.mark_as_done()
    assert task.done is True


def test_mark_as_done_already_done():
    task = Task("Buy groceries", "Need to buy milk, eggs, and bread", date(2025, 12, 31))
    task.done = True
    
    with pytest.raises(TaskWasAlreadyDoneError):
        task.mark_as_done()
