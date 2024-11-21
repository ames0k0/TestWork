from enum import Enum

from kafka import KafkaProducer

from src.logging.app import get_producer


class TopicEnum(str, Enum):
    TARIFF = "TARIFF"


class UserEventsLogger:
    producer: KafkaProducer = get_producer()

    def log(
        self,
        user_id: int | None,
        event_topic: TopicEnum, event_message: str, event_timestamp: float,
    ):
        self.producer.send(
            key=str(user_id).encode(),
            value=event_message.encode(),
            timestamp_ms=int(event_timestamp),
            topic=event_topic,
        )
        self.producer.flush()
