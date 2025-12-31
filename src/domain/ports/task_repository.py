from typing import Protocol, List, Optional
from src.domain.task import Task


class TaskRepositoryProtocol(Protocol):
    def save(self, task: Task) -> Task:
        """Upsert a task (update if exists, insert if not)"""
        ...

    def list(self) -> List[Task]:
        """List all tasks"""
        ...

    def get(self, task_id: str) -> Optional[Task]:
        """Get a task by ID"""
        ...

    def delete(self, task_id: str) -> None:
        """Delete a task by ID"""
        ...
