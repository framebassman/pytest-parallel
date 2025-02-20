import logging
from logging import Logger

import pytest


@pytest.fixture(scope="session")
def logger() -> Logger:
    return logging.getLogger()
