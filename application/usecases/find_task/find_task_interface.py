from abc import ABC, abstractmethod
from dataclasses import dataclass
from src.domain.task import Task


@dataclass(frozen=True)
class FindTaskRequest:
    task_id: str


@dataclass(frozen=True)
class FindTaskResponse:
    task: Task |


class FindTaskInterface(ABC):
    @abstractmethod
    def execute(self, request: FindTaskRequest) -> FindTaskResponse:
        """Find a task by ID"""
        ...
