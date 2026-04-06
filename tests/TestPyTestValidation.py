# Fixtures
import pytest


@pytest.fixture
def preWork():
    print("I setup browser instance")


def test_initialCheck(preWork):
    print("First test")


def test_secondCheck(preWork):
    assert 2 == 3
    print("Second test")
