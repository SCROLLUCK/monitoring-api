import asyncio
from fastapi import FastAPI

from src.infra.messengers.mqtt.llistener import MQTTListener
from src.presentation.exception_handler import (
    http_exception_handler,
    validation_exception_handler,
)

from src.infra.persistence.database_setup import DatabaseHandler
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from src.application.exceptions.base_exception import HTTPException
from fastapi.exceptions import RequestValidationError
from contextlib import asynccontextmanager
from src.presentation.routers.monitoring_router import monitoring_router
from src.utils.init_services import init_services


tags_metadata = [{"name": "Monitoring", "description": "Monitoring"}]



@asynccontextmanager
async def lifespan(app: FastAPI):
    await DatabaseHandler.connect(app)
    init_services()
    # MQTTListener()
    yield



app = FastAPI(
    title="API de Monitoramento",
    description="API de monitoramento de sensores ambientais",
    version="1.0.0",
    contact={
        "name": "Lucas Castro",
        "url": "https://github.com/SCROLLUCK",
        "email": "lucasluck77.ll@gmail.com",
    },
    lifespan=lifespan,
    openapi_tags=tags_metadata,
    # servers=[
    #     {"url": "https://esdgrd.flex-am.com.br", "description": "Subdomínio ESDGRD"},
    # ],
    root_path="/",
)


app.include_router(monitoring_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.add_exception_handler(HTTPException, handler=http_exception_handler)
app.add_exception_handler(RequestValidationError, handler=validation_exception_handler)


@app.get("/", include_in_schema=False)
async def docs_redirect():
    return RedirectResponse(url="/docs")
