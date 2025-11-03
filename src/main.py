import os
import asyncio
from dotenv import load_dotenv


load_dotenv()
config = os.environ


def start():
    import uvicorn
    from src.presentation.fastapi_setup import app

    loop = asyncio.new_event_loop()

    config_server = uvicorn.Config(
        app=app,
        loop="auto",
        port=int(config["API_PORT"]),
        host=config["API_HOST"],
        lifespan="on",
        reload=True,
        log_config=uvicorn.config.LOGGING_CONFIG,
    )
    server = uvicorn.Server(config_server)
    loop.run_until_complete(server.serve())


if __name__ == "__main__":
    start()
