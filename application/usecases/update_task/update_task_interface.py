from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import date
from src.domain.task import Task


@dataclass(frozen=True)
class UpdateTaskRequest:
    task_id: str
    title: str | None = None
    description: str | None = None
    due_date: date | None = None


@dataclass(frozen=True)
class UpdateTaskResponse:
    task: Task


class UpdateTaskInterface(ABC):
    @abstractmethod
    def execute(self, request: UpdateTaskRequest) -> UpdateTaskResponse:
        """Update a task"""
        ...
