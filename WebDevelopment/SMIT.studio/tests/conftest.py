import os

import pytest

from src.core import config


@pytest.fixture(scope="module")
def clean_up_files(_):
    fps = (
        config.INSURANCE_RATE_FILEPATH,
        config.DATABASE_FILEPATH
    )
    for fp in fps:
        if fp.exists():
            os.remove(fp)

    yield

    for fp in fps:
        if fp.exists():
            os.remove(fp)
