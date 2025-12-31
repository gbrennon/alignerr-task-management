from dataclasses import dataclass
from src.domain.task import Task
from src.domain.ports.task_repository import TaskRepositoryProtocol


@dataclass(frozen=True)
class FindTaskRequest:
    task_id: str


@dataclass(frozen=True)
class FindTaskResponse:
    task: Task |


class FindTaskPort:
    def __init__(self, repository: TaskRepositoryProtocol):
        self.repository = repository

    def execute(self, request: FindTaskRequest) -> FindTaskResponse:
        task = self.repository.get(request.task_id)
        return FindTaskResponse(task=task)
