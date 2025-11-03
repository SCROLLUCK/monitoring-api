import inspect
from types import NoneType
from typing import Type, Annotated, get_args

from fastapi import Form
from fastapi.params import Form as FormParam
from pydantic import BaseModel
from pydantic.fields import FieldInfo


def to_camel_case(string: str) -> str:
    return "".join(
        word.capitalize() if i > 0 else word for i, word in enumerate(string.split("_"))
    )


class DTOBaseModel(BaseModel):
    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        alias_generator = to_camel_case
        str_min_length = 1
        str_strip_whitespace = True