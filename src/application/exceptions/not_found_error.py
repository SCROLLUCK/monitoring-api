import uuid

from src.application.exceptions.base_exception import ExceptionMetadata, HTTPException
from src.application.exceptions.error_factory import ErrorFactory


class NotFoundException(HTTPException):
    title: str = "NotFoundException"
    status_code: int = 404


class UserDoesExistsInDatabase(ExceptionMetadata):
    name: str = "notFound.userDoesExistsInDatabase"
    message: str = "The user exists in the database."
    default_fields: dict = {
        "field": "registration",
        "value": uuid.uuid4(),
        "location": "BODY",
    }


class UserUUIDNotFound(ExceptionMetadata):
    name: str = "notFound.UserUUIDNotFound"
    message: str = "The user id not found in the database"
    default_fields: dict = {
        "field": "id",
        "value": uuid.uuid4(),
        "location": "BODY",
    }


class EquipmentUUIDNotFound(ExceptionMetadata):
    name: str = "notFound.equipmentUUIDNotFound"
    message: str = "The equipment id not found in the database"
    default_fields: dict = {
        "field": "id",
        "value": uuid.uuid4(),
        "location": "BODY",
    }


class CompanyUUIDNotFound(ExceptionMetadata):
    name: str = "notFound.companyUUIDNotFound"
    message: str = "The company id not found in the database"
    default_fields: dict = {
        "field": "id",
        "value": uuid.uuid4(),
        "location": "BODY",
    }


class LineUUIDNotFound(ExceptionMetadata):
    name: str = "notFound.lineUUIDNotFound"
    message: str = "The line id not found in the database"
    default_fields: dict = {
        "field": "id",
        "value": uuid.uuid4(),
        "location": "BODY",
    }


class EventMaintenanceUUIDNotFound(ExceptionMetadata):
    name: str = "notFound.eventMaintenanceUUIDNotFound"
    message: str = "The event maintenance id not found in the database"
    default_fields: dict = {
        "field": "id",
        "value": uuid.uuid4(),
        "location": "BODY",
    }


class EventUUIDNotFound(ExceptionMetadata):
    name: str = "notFound.eventUUIDNotFound"
    message: str = "The event id not found in the database"
    default_fields: dict = {
        "field": "id",
        "value": uuid.uuid4(),
        "location": "BODY",
    }


class EventDataNotFound(ExceptionMetadata):
    name: str = "notFound.eventDataNotDound"
    message: str = "Event data is empty"
    default_fields: dict = {
        "field": "data",
        "value": uuid.uuid4(),
        "location": "BODY",
    }


class LineKeyNotFound(ExceptionMetadata):
    name: str = "notFound.lineKeyNotFound"
    message: str = "Line key doenst exists on Redis"
    default_fields: dict = {
        "field": "data",
        "value": uuid.uuid4(),
        "location": "BODY",
    }


UserDoesExistsInDatabaseError = ErrorFactory.create(
    NotFoundException, UserDoesExistsInDatabase
)

UserUUIDNotFoundError = ErrorFactory.create(NotFoundException, UserUUIDNotFound)

EquipmentUUIDNotFoundError = ErrorFactory.create(
    NotFoundException, EquipmentUUIDNotFound
)

CompanyUUIDNotFoundError = ErrorFactory.create(NotFoundException, CompanyUUIDNotFound)

LineUUIDNotFoundError = ErrorFactory.create(NotFoundException, LineUUIDNotFound)

EventMaintenanceUUIDNotFoundError = ErrorFactory.create(
    NotFoundException, EventMaintenanceUUIDNotFound
)

EventUUIDNotFoundError = ErrorFactory.create(NotFoundException, EventUUIDNotFound)

EventDataNotFoundError = ErrorFactory.create(NotFoundException, EventDataNotFound)

LineKeyNotFoundError = ErrorFactory.create(NotFoundException, LineKeyNotFound)
