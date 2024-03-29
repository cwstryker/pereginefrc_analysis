from os import getenv

import pytest

from peregrinefrc_analysis.peregrine_client import PeregrineClient

VALID_EVENT = "2023orwil"
VALID_EVENT_SHAPE_2023 = (28, 9)
INVALID_EVENT = "2023zzzzz"


@pytest.fixture(scope="module")
def unauthenticated_client():
    """This client does not have an access token assigned"""
    return PeregrineClient()


@pytest.fixture(scope="module")
def authenticated_client():
    """This client does not have an access token assigned"""
    client = PeregrineClient()
    username = getenv("PEREGRINE_USERNAME")
    password = getenv("PEREGRINE_PASSWORD")
    client.authenticate(username=username, password=password)
    return client


@pytest.fixture(scope="module")
def reports_data(authenticated_client):
    return authenticated_client.event_reports(VALID_EVENT)
