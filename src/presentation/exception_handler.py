import logging

from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from src.application.exceptions.base_exception import HTTPException

alpha_logger = logging.getLogger("alpha_logger")


async def http_exception_handler(request: Request, exc: HTTPException):
    alpha_logger.error(
        f"[{exc.title} - {exc.status_code}]: "
        f"{jsonable_encoder(exc.exceptions)}"
    )
    return JSONResponse(
        status_code=exc.status_code,
        content=jsonable_encoder(dict(title=exc.title, errors=exc.exceptions)),
    )


async def validation_exception_handler(
    request: Request, exc: RequestValidationError
):
    errors = []
    status_code = 422
    title_ = (
            exc.errors()[0].get("type").replace("_", " ").title().replace(
                " ", ""
            )
            + "Exception"
    )
    for exception in exc.errors():
        title = (
                exception.get("type").replace("_", " ").title().replace(" ", "")
                + "Exception"
        )
        location = exception.get("loc")[0].upper()
        code = f"semantic.{title[:1].lower() + title[1:]}"
        message = exception.get("msg")
        field = (
            exception.get("loc")[1] if len(exception.get("loc")) > 1 else None
        )
        value = exception.get("input")

        error = dict(
            location=location,
            code=code,
            message=message,
            field=field,
            value=value,
        )

        errors.append(error)

        alpha_logger.error(
            f"[{title} - {status_code}]: " f"{jsonable_encoder(error)}"
        )

    return JSONResponse(
        status_code=status_code,
        content=dict(title=title_, errors=jsonable_encoder(errors)),
    )
