from fastapi import APIRouter

from src.application.dto.requests.monitoring import MonitoringRequest
from src.application.dto.responses.monitoring import MonitoringResponse
from src.application.services.monitoring_service import MonitoringService


monitoring_router = APIRouter(prefix="/monitoring",tags=["Monitoring"])

@monitoring_router.get('/', response_model=list[MonitoringResponse])
async def get_messages():
  monitoring_data = await MonitoringService.get_messages()
  return monitoring_data

@monitoring_router.post("/")
async def publish_message(monitoring_request: MonitoringRequest):
  await MonitoringService.publish_message(monitoring_request)
  
  return monitoring_request