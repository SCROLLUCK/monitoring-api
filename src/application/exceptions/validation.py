from src.application.exceptions.base_exception import (
    HTTPException,
    ExceptionMetadata,
)
from src.application.exceptions.error_factory import ErrorFactory

class ValidationException(HTTPException):
    title: str = "ValidationException"
    status_code: int = 400

class PhoneInvalidFormat(ExceptionMetadata):
    name: str = "validation.phoneInvalidFormat"
    message: str = "Phone invalid format -> 5592999999999 / (55) 92999999999 / +55 11 91234-5678"
    default_fields: dict = {
        "field": "phone",
        "value": "5592999999999",
        "location": "BODY",
    }

class DateOutOfRange(ExceptionMetadata):
    name: str = "validation.dateOutOfRange"
    message: str = "Data inicial não pode ser maior que a data atual"
    default_fields: dict = {
        "field": "end_date",
        "value": "data maior que data atual",
        "location": "BODY",
    }

class DateInitialOutOfRange(ExceptionMetadata):
    name: str = "validation.dateOutOfRange"
    message: str = "A data inicial não pode ser maior que a data final."
    default_fields: dict = {
        "field": "end_date",
        "value": "data maior que data atual",
        "location": "BODY",
    }

PhoneInvalidFormatError = ErrorFactory.create(
    ValidationException, PhoneInvalidFormat
)

DateOutOfRangeError = ErrorFactory.create(
    ValidationException, DateOutOfRange
)

DateInitialOutOfRangeError = ErrorFactory.create(
    ValidationException, DateInitialOutOfRange
)