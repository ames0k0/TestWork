from kafka import KafkaProducer

from src.core import config

producer = None


def initialize():
    global producer

    producer = KafkaProducer(
        bootstrap_servers=config.KAFKA_PRODUCER_BOOTSTRAP_SERVERS,
    )


def get_producer():
    if producer is None:
        initialize()

    return producer
