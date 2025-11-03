
from datetime import datetime
from uuid import UUID
from pydantic import BaseModel


class Monitoring(BaseModel):
  id_: UUID
  timestamp: datetime
  temperature: float
  humidity: float