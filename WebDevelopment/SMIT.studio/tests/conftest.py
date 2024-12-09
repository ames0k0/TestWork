from src.database.app import SQL
from src.logging.app import Kafka


def pytest_configure(config):
  SQL.initialize()
  Kafka.initialize()
