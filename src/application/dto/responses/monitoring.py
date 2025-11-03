from datetime import datetime
from uuid import UUID
from src.application.dto.base_dto import DTOBaseModel


class MonitoringResponse(DTOBaseModel):
  id_: UUID
  timestamp: datetime
  temperature: float
  humidity: float