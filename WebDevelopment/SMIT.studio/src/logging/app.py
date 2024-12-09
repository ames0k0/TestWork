from kafka import KafkaProducer

from src.core import config


__all__ = (
    'Kafka',
)


class Kafka:
    producer = None

    @classmethod
    def initialize(cls):
        """Initialize KafkaProducer
        """
        cls.producer = KafkaProducer(
            bootstrap_servers=config.KAFKA_PRODUCER_BOOTSTRAP_SERVERS,
        )
