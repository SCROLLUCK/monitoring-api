from src.application.exceptions.base_exception import (
    HTTPException,
    ExceptionMetadata,
)
from src.application.exceptions.error_factory import ErrorFactory


class UnauthorizedException(HTTPException):
    title: str = "UnauthorizedException"
    status_code: int = 401


class AccessDenied(ExceptionMetadata):
    name: str = "unauthorized.accessDenied"
    message: str = "Access denied: just administrators."
    default_fields: dict = {
        "field": "is_admin",
        "value": False,
        "location": "Body",
    }


class InvalidUser(ExceptionMetadata):
    name: str = "unauthorized.invalidUser"
    message: str = "The registration or password provided is invalid."
    default_fields: dict = {
        "field": "user",
        "value": "12314",
        "location": "HEADER",
    }


class InvalidRegistration(ExceptionMetadata):
    name: str = "unauthorized.invalidRegistration"
    message: str = "The registration provided is invalid."
    default_fields: dict = {
        "field": "registration",
        "value": "12314",
        "location": "HEADER",
    }


class InvalidPassword(ExceptionMetadata):
    name: str = "unauthorized.invalidPassword"
    message: str = "The password provided is invalid."
    default_fields: dict = {
        "field": "password",
        "value": "-",
        "location": "HEADER",
    }


class InvalidToken(ExceptionMetadata):
    name: str = "unauthorized.invalidToken"
    message: str = "The token provided is invalid."
    default_fields: dict = {
        "field": "token",
        "value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
        ".eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI"
        "6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDI"
        "yfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6y"
        "JV_adQssw5c",
        "location": "HEADER",
    }


class ExpiredToken(ExceptionMetadata):
    name: str = "unauthorized.expiredToken"
    message: str = "The token provided is expired."
    default_fields: dict = {
        "field": "token",
        "value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
        ".eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI"
        "6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDI"
        "yfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6y"
        "JV_adQssw5c",
        "location": "HEADER",
    }


class UnauthorizedUser(ExceptionMetadata):
    name: str = "unauthorized.unauthorizedUser"
    message: str = "The token provided is expired."
    default_fields: dict = {
        "field": "token",
        "value": False,
        "location": "HEADER",
    }


class InactiveLine(ExceptionMetadata):
    name: str = "unauthorized.inactiveLine"
    message: str = "Line Inactive"
    default_fields: dict = {
        "field": "is_active",
        "value": False,
        "location": "BODY",
    }


InvalidUserError = ErrorFactory.create(UnauthorizedException, InvalidUser)
InvalidProvidedTokenError = ErrorFactory.create(UnauthorizedException, InvalidToken)
InvalidRegistrationError = ErrorFactory.create(
    UnauthorizedException, InvalidRegistration
)
InvalidPasswordError = ErrorFactory.create(UnauthorizedException, InvalidPassword)
ExpiredTokenError = ErrorFactory.create(UnauthorizedException, ExpiredToken)
UnauthorizedUserError = ErrorFactory.create(UnauthorizedException, UnauthorizedUser)
AccessDeniedError = ErrorFactory.create(UnauthorizedException, AccessDenied)
InactiveLineError = ErrorFactory.create(UnauthorizedException, InactiveLine)
