
from typing import Type
from uuid import uuid4

from src.application.dto.requests.monitoring import MonitoringRequest
from src.application.dto.responses.monitoring import MonitoringResponse
from src.domain.models.monitoring import Monitoring
from src.domain.repositories.monitoring_repository_interface import IMonitoringRepository
from src.infra.persistence.repository.monitoring_repository import MonitoringRepository


class MonitoringService:
  
  monitoring_repository: Type[IMonitoringRepository]
  def __new__(cls,monitoring_repository: Type[IMonitoringRepository]):
    cls.monitoring_repository = monitoring_repository
    return cls
  
  @classmethod
  async def publish_message(cls, monitoring_request: MonitoringRequest):
    new_monitoring = Monitoring(**monitoring_request.model_dump(), id_=uuid4())
    await cls.monitoring_repository.publish_message(new_monitoring)
    
  @classmethod
  async def get_messages(cls):
    monitoring_data = await cls.monitoring_repository.get_messages()
    data = [MonitoringResponse(**monitoring.model_dump()) for monitoring in monitoring_data]
    return data