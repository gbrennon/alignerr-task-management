from dataclasses import dataclass
from src.domain.task import Task
from src.domain.ports.task_repository import TaskRepositoryProtocol


@dataclass(frozen=True)
class CompleteTaskRequest:
    task_id: str


@dataclass(frozen=True)
class CompleteTaskResponse:
    task: Task


class CompleteTaskPort:
    def __init__(self, repository: TaskRepositoryProtocol):
        self.repository = repository

    def execute(self, request: CompleteTaskRequest) -> CompleteTaskResponse:
        task = self.repository.save(request)
        return CompleteTaskResponse(task=task)
