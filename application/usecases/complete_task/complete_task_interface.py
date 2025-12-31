from abc import ABC, abstractmethod
from dataclasses import dataclass
from src.domain.task import Task


@dataclass(frozen=True)
class CompleteTaskRequest:
    task_id: str


@dataclass(frozen=True)
class CompleteTaskResponse:
    task: Task


class CompleteTaskInterface(ABC):
    @abstractmethod
    def execute(self, request: CompleteTaskRequest) -> CompleteTaskResponse:
        """Complete a task"""
        ...
