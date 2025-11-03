from src.application.exceptions.base_exception import (
    HTTPException,
    ExceptionMetadata,
)
from src.application.exceptions.error_factory import ErrorFactory


class ForbiddenException(HTTPException):
    title: str = "ForbiddenException"
    status_code: int = 403


class UserCannotChangeOwnRole(ExceptionMetadata):
    name: str = "validation.userCannotChangeOwnRole"
    message: str = (
        "Use cant change your role, only an admin user can change the role of another user."
    )
    default_fields: dict = {
        "field": "admin",
        "value": False,
        "location": "BODY",
    }


class UserCannotSelfDelete(ExceptionMetadata):
    name: str = "validation.userCannotSelfDelete"
    message: str = "Use cannot delete yourself, an admin user can delete another user."
    default_fields: dict = {
        "field": "user",
        "value": "",
        "location": "BODY",
    }


UserCannotChangeOwnRoleError = ErrorFactory.create(
    ForbiddenException, UserCannotChangeOwnRole
)

UserCannotSelfDeleteError = ErrorFactory.create(
    ForbiddenException, UserCannotSelfDelete
)
