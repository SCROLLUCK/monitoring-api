from typing import Any, Literal, Optional

from pydantic import BaseModel


class ExceptionMetadata(BaseModel):
    name: Optional[str] = None
    message: Optional[str] = None
    default_fields: Optional[dict] = None


class ExceptionEntity(BaseModel):
    location: Literal["BODY", "HEADER", "QUERY", "PATH"] = "BODY"
    code: str
    message: str
    field: str
    value: Any

    @classmethod
    def from_exception_model(cls, error: "ExceptionModel"):
        assert isinstance(error.field, str)
        assert isinstance(error.metadata.name, str)
        assert isinstance(error.metadata.message, str)
        return cls(
            location=error.location,
            code=error.metadata.name,
            message=error.metadata.message,
            field=error.field,
            value=error.value,
        )


class ExceptionModel(BaseModel):
    location: Literal["BODY", "HEADER", "QUERY", "PATH"] = "BODY"
    metadata: ExceptionMetadata
    field: Optional[str] = None
    value: Optional[Any] = None

    def get_exception_entity(self) -> ExceptionEntity:
        assert isinstance(self.metadata.default_fields, dict)
        for field, value in self.metadata.default_fields.items():
            if getattr(self, field) is None:
                setattr(self, field, value)

        return ExceptionEntity.from_exception_model(self)


class HTTPException(Exception):
    title: str = "HTTPException"
    status_code: int = 400
    exceptions: list[ExceptionEntity]

    def __init__(self) -> None:
        super().__init__()
        self.exceptions = []

    def __call__(self, *args, **kwargs):
        if args:
            self.exceptions[0].message = args[0]

        if "value" in kwargs:
            setattr(self.exceptions[0], "value", kwargs["value"])
        if "field" in kwargs:
            setattr(self.exceptions[0], "field", kwargs["field"])
        return self

    def get_model(self) -> ExceptionEntity:
        return self.exceptions[0]

    def add_error(self, exception: ExceptionModel):
        self.exceptions.append(exception.get_exception_entity())
