import pytest


@pytest.fixture
def number():
    return 11111123


@pytest.fixture
def empty_string():
    return ""


@pytest.fixture
def card_number1():
    return 7000792289606361


@pytest.fixture
def card_number2():
    return "7000792289606361"


@pytest.fixture
def card_number3():
    return "7B00792289606361"


@pytest.fixture
def account1():
    return 73654108430135874305


@pytest.fixture
def account2():
    return "73654108430135874305"


@pytest.fixture
def account3():
    return "736A4108430135874305"
