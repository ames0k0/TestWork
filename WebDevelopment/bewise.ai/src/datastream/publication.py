import json
from enum import Enum

from src.database import models
from . import app


class TopicEnum(str, Enum):
    KAFKA = "Kafka"


class Kafka:
    @staticmethod
    async def publish_new_application(obj: models.Application):
        await app.Kafka.producer.send(
            topic=TopicEnum.KAFKA.value,
            value=json.dumps({
                "id": obj.id,
                "user_name": obj.user_name,
                "description": obj.description,
                "created_at": str(obj.created_at),
            }).encode(),
        )
