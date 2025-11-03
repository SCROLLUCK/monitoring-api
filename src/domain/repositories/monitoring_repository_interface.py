from abc import abstractmethod, ABC

from src.domain.models.monitoring import Monitoring

class IMonitoringRepository(ABC):
  @classmethod
  @abstractmethod
  async def publish_message(cls, monitoring: Monitoring):
    raise NotImplementedError
  
  @classmethod
  @abstractmethod
  async def get_messages(cls):
    raise NotImplementedError