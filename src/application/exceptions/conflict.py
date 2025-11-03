from src.application.exceptions.base_exception import ExceptionMetadata, HTTPException
from src.application.exceptions.error_factory import ErrorFactory


class ConflictException(HTTPException):
    title: str = "ConflictException"
    status_code: int = 409


class RegistrationIsAlreadyInDatabase(ExceptionMetadata):
    name: str = "conflict.registrationIsAlreadyInDatabase"
    message: str = "The registration is already in database."
    default_fields: dict = {
        "field": "registration",
        "value": "12345",
        "location": "BODY",
    }


class EmailIsAlreadyInDatabase(ExceptionMetadata):
    name: str = "conflict.emailIsAlreadyInDatabase"
    message: str = "The email is already in database."
    default_fields: dict = {
        "field": "email",
        "value": "john.doe@example.com",
        "location": "BODY",
    }


class PhoneIsAlreadyInDatabase(ExceptionMetadata):
    name: str = "conflict.phoneIsAlreadyInDatabase"
    message: str = "The phone is already in database."
    default_fields: dict = {
        "field": "phone",
        "value": "92999999999",
        "location": "BODY",
    }


class EquipmentOnIsAlreadyInDatabase(ExceptionMetadata):
    name: str = "conflict.equipmentOnIsAlreadyInDatabase"
    message: str = "The equipment in line is already  in database."
    default_fields: dict = {
        "field": "equipmentId",
        "value": "uuid",
        "location": "BODY",
    }


class LineNameIsAlreadyInDatabase(ExceptionMetadata):
    name: str = "conflict.lineNameIsAlreadyInDatabase"
    message: str = "Line name is already in database"
    default_fields: dict = {
        "field": "name",
        "value": "Line Name",
        "location": "BODY",
    }


class EquipmentWithLineAlreadyExists(ExceptionMetadata):
    name: str = "conflict.equipmentWithLineAlreadyExists"
    message: str = "Equipment with line already exists"
    default_fields: dict = {
        "field": "equipment_id",
        "value": "Equipment id",
        "location": "BODY",
    }


class EventMaintenanceInEventAlreadyExists(ExceptionMetadata):
    name: str = "conflict.eventMaintenanceInEventAlreadyExists"
    message: str = "Event maintenance in event already exists"
    default_fields: dict = {
        "field": "event id",
        "value": "event id",
        "location": "BODY",
    }


RegistrationIsAlreadyInDatabaseError = ErrorFactory.create(
    ConflictException, RegistrationIsAlreadyInDatabase
)

EmailIsAlreadyInDatabaseError = ErrorFactory.create(
    ConflictException, EmailIsAlreadyInDatabase
)

PhoneIsAlreadyInDatabaseError = ErrorFactory.create(
    ConflictException, PhoneIsAlreadyInDatabase
)

EquipmentOnIsAlreadyInDatabaseError = ErrorFactory.create(
    ConflictException, EquipmentOnIsAlreadyInDatabase
)

LineNameIsAlreadyInDatabaseError = ErrorFactory.create(
    ConflictException, LineNameIsAlreadyInDatabase
)

EquipmentWithLineAlreadyExistsError = ErrorFactory.create(
    ConflictException, EquipmentWithLineAlreadyExists
)

EventMaintenanceInEventAlreadyExistsError = ErrorFactory.create(
    ConflictException, EventMaintenanceInEventAlreadyExists
)
