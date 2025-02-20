import logging
from logging import Logger

import pytest


@pytest.fixture(scope="session")
def logger(pytestconfig, worker_id) -> Logger:
    if worker_id is not None:
        logging.basicConfig(
            format=pytestconfig.getini("log_file_format"),
            filename=f"tests_{worker_id}.log",
            level=pytestconfig.getini("log_file_level"),
        )
    return logging.getLogger()
