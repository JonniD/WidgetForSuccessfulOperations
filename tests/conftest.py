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

@pytest.fixture
def card1():
    return "Maestro 1596837868705199"

@pytest.fixture
def card2():
    return "Visa Classic 6831982476737658"

@pytest.fixture
def card3():
    return "MasterCard 7158300734726758"
@pytest.fixture
def account1():
    return "Счет 64686473678894779589"

@pytest.fixture
def account2():
    return "Счет 35383033474447895560"
@pytest.fixture
def date():
    return "2024-03-11T02:26:18.671407"