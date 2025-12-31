class TaskWasAlreadyDoneError(Exception):
    """Exception raised when trying to mark a task as done that is already done."""
    pass
