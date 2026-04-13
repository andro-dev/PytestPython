import pytest


@pytest.fixture(scope="session")
def preWork():
    print("I setup browser instance")
    