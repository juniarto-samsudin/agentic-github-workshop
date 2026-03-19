# Copilot Custom Instructions for Todo API

## Language & Documentation

- Write all code comments and docstrings in **English**
- Use **Google-style** docstrings and always include:
  - Function summary (first line)
  - Args section (if parameters exist)
  - Returns section (if there is a return value)
  - Raises section (if exceptions are raised)
  - Example section showing a sample usage or curl command

## Coding Conventions

- Use Python 3.11+ type hints on **all functions** without exception
- Use `X | None` format instead of `Union` or `Optional`
- Use snake_case for variables and functions, PascalCase for classes
- Never use magic numbers — define named constants instead

## Error Handling

- All API error responses must use this unified format:
  ```json
  {
    "error": {
      "code": "ERROR_CODE",
      "message": "A human-readable error message",
      "details": {}
    }
  }
  ```
- Error codes must use UPPER_SNAKE_CASE (e.g., `TODO_NOT_FOUND`, `INVALID_INPUT`)
- Use custom exception classes instead of HTTPException

## API Design

- Specify `response_model` explicitly on all endpoints
- Implement pagination parameters (`skip`, `limit`) on all list endpoints
- Default `limit` is 20, maximum is 100
- Include `X-Total-Count` header in list responses

## Testing

- Use pytest as the test framework
- Place test files in the `tests/` directory
- Name test functions as `test_<target>_<condition>_<expected_result>`
  - Example: `test_create_todo_with_valid_data_returns_201`
  - Example: `test_get_todo_with_invalid_id_returns_404`
- Include a docstring in each test function describing **the purpose of the test**
- Ensure test isolation by resetting the database before each test

## Logging

- Log every endpoint request
- Log format: `[{method}] {path} - {status_code} ({elapsed}ms)`
- Use Python's standard `logging` module
