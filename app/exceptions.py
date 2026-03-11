"""Todo APIのカスタム例外クラス。

HTTPExceptionの代わりにカスタム例外クラスを使用し、
統一されたエラーレスポンス形式を提供する。
"""


class AppException(Exception):
    """アプリケーション例外の基底クラス。

    Args:
        code: アッパースネークケースのエラーコード
        message: 人間が読めるエラーメッセージ
        status_code: HTTPステータスコード
        details: エラーの詳細情報
    """

    def __init__(
        self,
        code: str,
        message: str,
        status_code: int,
        details: dict | None = None,
    ) -> None:
        self.code = code
        self.message = message
        self.status_code = status_code
        self.details = details or {}
        super().__init__(message)


class TodoNotFoundException(AppException):
    """指定されたIDのTodoが見つからない場合の例外。

    Args:
        todo_id: 見つからなかったTodoのID
    """

    def __init__(self, todo_id: int) -> None:
        super().__init__(
            code="TODO_NOT_FOUND",
            message=f"Todo with id {todo_id} not found",
            status_code=404,
            details={"todo_id": todo_id},
        )


class InvalidInputException(AppException):
    """入力データが不正な場合の例外。

    Args:
        message: エラーメッセージ
        details: バリデーションエラーの詳細
    """

    def __init__(self, message: str, details: dict | None = None) -> None:
        super().__init__(
            code="INVALID_INPUT",
            message=message,
            status_code=422,
            details=details or {},
        )
