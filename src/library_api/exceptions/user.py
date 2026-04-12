from .base import AppException


class UserException(AppException):
    pass


class UserNotFound(UserException):
    message = "User not found"


class UserAlreadyExists(UserException):
    message = "This user already exists"
