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
        event_topic: TopicEnum, event_message: str, event_timestamp: float,
    ):
        Kafka.producer.send(
            key=str(user_id).encode(),
            value=event_message.encode(),
            timestamp_ms=int(event_timestamp),
            topic=event_topic,
        )
        Kafka.producer.flush()
