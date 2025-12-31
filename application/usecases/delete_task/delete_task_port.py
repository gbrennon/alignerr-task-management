from dataclasses import dataclass
from src.domain.ports.task_repository import TaskRepositoryProtocol


@dataclass(frozen=True)
class DeleteTaskRequest:
    task_id: str


@dataclass(frozen=True)
class DeleteTaskResponse:
    pass


class DeleteTaskPort:
    def __init__(self, repository: TaskRepositoryProtocol):
        self.repository = repository

    def execute(self, request: DeleteTaskRequest) -> DeleteTaskResponse:
        self.repository.delete(request.task_id)
