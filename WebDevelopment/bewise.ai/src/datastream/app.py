from aiokafka import AIOKafkaProducer

from src.core import config


class Kafka:
    producer: AIOKafkaProducer = None

    @classmethod
    async def initialize(cls):
        cls.producer = AIOKafkaProducer(
            bootstrap_servers=config.KAFKA_PRODUCER_BOOTSTRAP_SERVERS,
        )
        await cls.producer.start()

    @classmethod
    async def terminate(cls):
        await cls.producer.stop()