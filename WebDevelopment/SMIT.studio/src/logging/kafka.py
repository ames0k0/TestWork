import json
import datetime as dt
from enum import Enum

from src.logging.app import Kafka


class TopicEnum(str, Enum):
    TARIFF = "TARIFF"


class UserEventsLogger:
    """Logging user events
    """
    @staticmethod
    def log_to_kafka(
        user_id: int | None,
        event_topic: TopicEnum, event_message: str, event_datetime: dt.datetime,
    ):
        Kafka.producer.send(
            topic=event_topic,
            value=json.dumps({
                "user_id": user_id,
                "event_message": event_message,
                "event_datetime": str(event_datetime),
            }).encode(),
        )
