from dataclasses import dataclass
from datetime import date
from src.domain.ports.task_repository import TaskRepositoryProtocol


@dataclass(frozen=True)
class CreateTaskRequest:
    title: str
    description: str
    due_date: date


@dataclass(frozen=True)
class CreateTaskResponse:
    task_id: str


class CreateTaskPort:
    def __init__(self, repository: TaskRepositoryProtocol):
        self.repository = repository

    def execute(self, request: CreateTaskRequest) -> CreateTaskResponse:
        task = self.repository.save(request)
        return CreateTaskResponse(task_id=task.id)
