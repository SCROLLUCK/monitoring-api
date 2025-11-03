from fastapi import APIRouter

from src.application.dto.requests.sensor import MonitoringRequest
from src.application.services.monitoring_service import MonitoringService


monitoring_router = APIRouter(prefix="/monitoring")

@monitoring_router.get('/')
async def get_messages():
  monitoring_data = await MonitoringService.get_messages()
  return monitoring_data

@monitoring_router.post("/")
async def publish_message(monitoring_request: MonitoringRequest):
  print(monitoring_request)
  await MonitoringService.publish_message(monitoring_request)
  
  return monitoring_request