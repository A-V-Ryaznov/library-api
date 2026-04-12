from .base import AppException


class CabinetException(AppException):
    pass


class CabinetNotFound(CabinetException):
    message = "Cabinet not found"


class CabinetAlreadyExists(CabinetException):
    message = "This cabinet already exists"
