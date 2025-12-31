from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List
from src.domain.task import Task


@dataclass(frozen=True)
class ListTasksRequest:
    pass


@dataclass(frozen=True)
class ListTasksResponse:
    tasks: List[Task]


class ListTasksInterface(ABC):
    @abstractmethod
    def execute(self, request: ListTasksRequest) -> ListTasksResponse:
        """List all tasks"""
        ...
