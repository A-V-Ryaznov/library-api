class AppException(Exception):
    message = "Unknown error"

    def __init__(self, message: str | None = None) -> None:
        super().__init__(message or self.message)
        self.message = message or self.message

    def __str__(self) -> str:
        return self.message
