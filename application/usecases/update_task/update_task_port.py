from dataclasses import dataclass
from datetime import date
from src.domain.task import Task
from src.domain.ports.task_repository import TaskRepositoryProtocol


@dataclass(frozen=True)
class UpdateTaskRequest:
    task_id: str
    title: str | None = None
    description: str | None = None
    due_date: date | None = None


@dataclass(frozen=True)
class UpdateTaskResponse:
    task: Task


class UpdateTaskPort:
    def __init__(self, repository: TaskRepositoryProtocol):
        self.repository = repository

    def execute(self, request: UpdateTaskRequest) -> UpdateTaskResponse:
        task = self.repository.save(request)
        return UpdateTaskResponse(task=task)
