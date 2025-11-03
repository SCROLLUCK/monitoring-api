from typing import Type

from src.application.exceptions.base_exception import (
    HTTPException,
    ExceptionMetadata,
    ExceptionModel,
)


class ErrorFactory:
    @classmethod
    def create(
        cls,
        exception_class: Type[HTTPException],
        exception_metadata: Type[ExceptionMetadata],
    ):
        metadata_instance = exception_metadata()
        http_exception_instance = exception_class()

        http_exception_instance.add_error(
            ExceptionModel(metadata=metadata_instance)
        )

        return http_exception_instance
