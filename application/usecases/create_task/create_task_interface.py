from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class CreateTaskRequest:
    title: str
    description: str
    due_date: date


@dataclass(frozen=True)
class CreateTaskResponse:
    task_id: str


class CreateTaskInterface(ABC):
    @abstractmethod
    def execute(self, request: CreateTaskRequest) -> CreateTaskResponse:
        """Create a new task"""
        ...
