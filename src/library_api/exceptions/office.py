from .base import AppException


class OfficeException(AppException):
    pass


class OfficeNotFound(OfficeException):
    message = "Office not found"


class OfficeAlreadyExists(OfficeException):
    message = "Office user already exists"
