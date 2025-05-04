import pytest

@pytest.fixture
def card_number() -> str:
    '''корректный номер карты'''
    return "7000792289606361"

@pytest.fixture
def account() -> str:
    '''корректный аккаунт'''
    return "73654108430135874305"

@pytest.fixture
def date_correct() -> str:
    '''корректная дата'''
    return "2024-03-11T02:26:18.671407"





