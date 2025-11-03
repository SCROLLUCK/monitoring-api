from src.domain.models.monitoring import Monitoring
from src.domain.repositories.monitoring_repository_interface import IMonitoringRepository
from src.infra.persistence.models.monitoring import MonitoringModel
from tortoise.transactions import in_transaction



class MonitoringRepository(IMonitoringRepository):
  
  @classmethod
  async def publish_message(cls, monitoring: Monitoring):
    async with in_transaction() as transaction:
      monitoring_data: MonitoringModel = MonitoringModel(
          id=monitoring.id_,
          timestamp=monitoring.timestamp,
          temperature=monitoring.temperature,
          humidity=monitoring.humidity
      )
      await monitoring_data.save(using_db=transaction)
      
  @classmethod
  async def get_messages(cls):
    monitoring_data = MonitoringModel.all()
    return monitoring_data