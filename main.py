from fastapi import FastAPI
from src.infra.persistence.database_setup import DatabaseSetup
from src.presentation.routers.monitoring_router import monitoring_router
from src.utils import init_services

app = FastAPI(
    title="Monitoramento ambiental",
    description="API de monitoramento de sensores ambientais",
    version="1.0.0",
    contact={'email': 'lucasluck77.ll@gmail.com', 'name': 'Lucas Castro'}
)

@app.on_event("startup")
async def startup_event():
    init_services.init_services()
    await DatabaseSetup.init_db()
    
    print("🚀 Application started!")

@app.on_event("shutdown")
async def shutdown_event():
    await DatabaseSetup.close_db()
    print("🛑 Application shutdown!")

# Incluir as rotas
app.include_router(monitoring_router) 

@app.get("/")
async def root():

    return {"message": "API de Monitoramento funcionando!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "database": "connected"}
