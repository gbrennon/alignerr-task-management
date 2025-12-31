# Alignerr Tasker

A simple task management API to help you organize and track your tasks.

## Features

This API provides a straightforward way to manage tasks with the following fields:

- **title**: The title of the task (string)
- **description**: A detailed description of the task (string)
- **done**: Boolean indicating if the task is completed (boolean)
- **due_date**: The due date for the task (date)

### Implemented Features

- Task domain entity with attributes: title, description, done, due_date
- `mark_as_done()` method that marks a task as done or raises `TaskWasAlreadyDoneError` if already done
- Unit tests for the Task entity and its methods (100% coverage)
- Repository port interface defining standard operations for task persistence
- Application layer with usecase ports implemented as services with repository injection:
  - CreateTaskPort
  - ListTasksPort  
  - FindTaskPort
  - UpdateTaskPort
  - CompleteTaskPort
  - DeleteTaskPort

## Getting Started

This project is currently in its initial setup phase. The API endpoints and implementation will be added in future commits.

## Project Structure

- `.git/` - Git version control
- `pyproject.toml` - Project configuration for UV
- `README.md` - This file
- `src/` - Source code
  - `domain/` - Domain entities and ports
    - `task.py` - Task entity implementation
    - `errors.py` - Custom error classes
    - `ports/` - Repository interfaces
      - `task_repository.py` - Task repository protocol
  - `application/` - Application layer
    - `usecases/` - Usecase ports and DTOs
      - `create_task/` - Create task usecase
        - `create_task_port.py` - Port with execute method and DTOs
      - `list_tasks/` - List tasks usecase
        - `list_tasks_port.py` - Port with execute method and DTOs
      - `find_task/` - Find task usecase
        - `find_task_port.py` - Port with execute method and DTOs
      - `update_task/` - Update task usecase
        - `update_task_port.py` - Port with execute method and DTOs
      - `complete_task/` - Complete task usecase
        - `complete_task_port.py` - Port with execute method and DTOs
      - `delete_task/` - Delete task usecase
        - `delete_task_port.py` - Port with execute method and DTOs
- `tests/` - Test cases
  - `domain/` - Tests for domain entities
    - `test_task.py` - Tests for Task entity

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues.

## License

This project is open source and available under an appropriate license to be determined.
