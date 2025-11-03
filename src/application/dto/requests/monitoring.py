from datetime import datetime

from src.application.dto.base_dto import DTOBaseModel

class MonitoringRequest(DTOBaseModel):
  timestamp: datetime
  temperature: float
  humidity: float