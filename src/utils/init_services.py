
from src.infra.persistence.repository.monitoring_repository import MonitoringRepository


def init_services():
  from src.application.services.monitoring_service import MonitoringService
  MonitoringService(MonitoringRepository)