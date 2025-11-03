from pydantic import BaseModel
from datetime import datetime

class MonitoringRequest(BaseModel):
  timestamp: datetime
  temperature: float
  humidity: float