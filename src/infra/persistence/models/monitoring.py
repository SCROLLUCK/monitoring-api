from tortoise.models import Model
from tortoise import fields

class DefaultModel(Model):
    
    id = fields.UUIDField(primary_key=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now_add=True)
    
    class Meta:
        abstract = True
    

class MonitoringModel(DefaultModel):
    timestamp = fields.DatetimeField()
    temperature = fields.FloatField()
    humidity = fields.FloatField()