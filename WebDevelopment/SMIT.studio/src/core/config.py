from pathlib import Path


STATIC_DIRECTORY = Path("src") / "static"
DATABASE_FILEPATH = STATIC_DIRECTORY / "sqlite3.db"
SQLALCHEMY_DATABASE_URL = "sqlite:///" + str(DATABASE_FILEPATH)
KAFKA_PRODUCER_BOOTSTRAP_SERVERS = "localhost:9092"

DEFAULT_USER_ID = 1
DEFAULT_CARGO_TYPE = "Other"

INSURANCE_RATE_DATE_FORMAT = "%Y-%m-%d"
INSURANCE_CALCULATION_EXAMPLES = [
    {
        "2020-06-01": [
            {
                "cargo_type": "Glass",
                "rate": "0.04"
            },
            {
                "cargo_type": "Other",
                "rate": "0.01"
            }
        ],
        "2020-07-01": [
            {
                "cargo_type": "Glass",
                "rate": "0.035"
            },
            {
                "cargo_type": "Other",
                "rate": "0.015"
            }
        ],
    }
]
