from pathlib import Path


DATABASE_FILEPATH = "sqlite:///./data/sqlite3.db"

STATIC_DIRECTORY = Path("src") / "static"

INSURANCE_RATE_FILEPATH = STATIC_DIRECTORY / "insurance_rate.json"
INSURANCE_RATE_DATE_FORMAT = "%Y-%m-%d"
DEFAULT_CARGO_TYPE = "other"

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
