"""Custom exception classes for the Todo API."""


class TodoNotFoundError(Exception):
    """Raised when a requested todo does not exist."""
