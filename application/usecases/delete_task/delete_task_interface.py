from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class DeleteTaskRequest:
    task_id: str


@dataclass(frozen=True)
class DeleteTaskResponse:
    pass


class DeleteTaskInterface(ABC):
    @abstractmethod
    def execute(self, request: DeleteTaskRequest) -> DeleteTaskResponse:
        """Delete a task"""
        ...
