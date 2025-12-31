from dataclasses import dataclass
from typing import List
from src.domain.task import Task
from src.domain.ports.task_repository import TaskRepositoryProtocol


@dataclass(frozen=True)
class ListTasksRequest:
    pass


@dataclass(frozen=True)
class ListTasksResponse:
    tasks: List[Task]


class ListTasksPort:
    def __init__(self, repository: TaskRepositoryProtocol):
        self.repository = repository

    def execute(self, request: ListTasksRequest) -> ListTasksResponse:
        tasks = self.repository.list()
        return ListTasksResponse(tasks=tasks)
