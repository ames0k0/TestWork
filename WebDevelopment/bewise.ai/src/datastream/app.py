from aiokafka import AIOKafkaProducer

from src.core.config import settings


class Kafka:
    producer: AIOKafkaProducer = None

    @classmethod
    async def initialize(cls):
        cls.producer = AIOKafkaProducer(
            bootstrap_servers=settings.kafka.BOOTSTRAP_SERVERS,
        )
        await cls.producer.start()

    @classmethod
    async def terminate(cls):
        await cls.producer.stop()
