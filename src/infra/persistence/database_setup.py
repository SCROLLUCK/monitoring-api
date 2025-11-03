import os
from src.main import config

from re import sub

import tortoise
from pydantic import BaseModel

from tortoise import Tortoise, fields

from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI
from tortoise.contrib.pydantic import pydantic_model_creator
from src.utils.logging import  logger

class DatabaseHandler:
    
    db_url = f'postgres://{os.getenv("POSTGRESQL_USERNAME")}:{os.getenv("POSTGRESQL_PASSWORD")}@{os.getenv("POSTGRESQL_HOST")}:{os.getenv("POSTGRESQL_PORT_NUMBER")}/{os.getenv("POSTGRESQL_DATABASE")}'
    CONFIG = {
        "connections": {
            "default": db_url,
        },
        "apps": {
            "models": {
                "models": ["src.infra.persistence.models"],
                "default_connection": "default"
            }
        }
    }

    @classmethod
    async def connect(cls, app: FastAPI):
        try:
            Tortoise.init_models(
                ["src.infra.persistence.models"],
                "models"
            )

            register_tortoise(
                app=app,
                db_url=cls.db_url,
                modules={
                    "models": ["src.infra.persistence.models"],
                },
                generate_schemas=True,
            )
            await Tortoise.init(config=cls.CONFIG)
            logger.info("✅ Database connection established")
        except Exception as e:
            logger.error("Error connecting to database:", str(e))
            raise

def snake_case(s):
    return '_'.join(
        sub(
            '([A-Z][a-z]+)', r' \1',
            sub(
                '([A-Z]+)', r' \1',
                s.removesuffix("Model").replace('-', ' ')
            )
        ).split()
    ).lower()


class IdMixin(tortoise.Model):
    id = fields.UUIDField(primary_key=True)
    
    class Meta:
        abstract = True


class TimestampMixin(IdMixin):
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    
    class Meta:
        abstract = True


class TortoiseModel(TimestampMixin):
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        
        if not cls._meta.abstract:
            cls._meta.db_table = snake_case(cls.__name__)
    
    async def to_pydantic(self) -> BaseModel:
        tortoise_pydantic = pydantic_model_creator(self.__class__)
        return await tortoise_pydantic.from_tortoise_orm(self)
    
    @classmethod
    async def from_pydantic(cls, model: BaseModel):
        return cls(
            **model.model_dump(exclude={"created_at"}),
            id=model.id_ if getattr(model, "id_") else model.id
        )
    
    class Meta:
        abstract = True
