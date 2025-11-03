from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise
import os

# Configuração do PostgreSQL
DB_CONFIG = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "host": os.getenv("POSTGRESQL_HOST", "localhost"),
                "port": os.getenv("POSTGRESQL_PORT_NUMBER", "5432"),
                "user": os.getenv("POSTGRESQL_USERNAME", "monitoring"),
                "password": os.getenv("POSTGRESQL_PASSWORD", "123"),
                "database": os.getenv("POSTGRESQL_DATABASE", "monitoring"),
            }
        }
    },
    "apps": {
        "models": {
            "models": ["src.infra.persistence.models"],  # APENAS a pasta models
            "default_connection": "default",
        }
    },
    "use_tz": False,
    "timezone": "UTC",
}

class DatabaseSetup:
    
    @staticmethod
    async def init_db():
        """Inicializar conexão com o banco de dados"""
        try:
            await Tortoise.init(config=DB_CONFIG)
            await Tortoise.generate_schemas()
            print("✅ Database initialized successfully!")
        except Exception as e:
            print(f"❌ Database initialization failed: {e}")
            raise
    
    @staticmethod
    async def close_db():
        """Fechar conexão com o banco de dados"""
        await Tortoise.close_connections()
        print("✅ Database connections closed!")
    
    @staticmethod
    def register_database(app):
        """Registrar o Tortoise no FastAPI"""
        register_tortoise(
            app,
            config=DB_CONFIG,
            generate_schemas=True,
            add_exception_handlers=True,
        )