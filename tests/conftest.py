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


@pytest.fixture
def processing_data() -> list[dict[str, str | int]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}
    ]


@pytest.fixture
def processing_data_wrong() -> list[dict[str, str | int]]:
    return [
        {"id": 41428829, "states": "NOTHING", "dates": "2019-07-038:35:29.512364"},
        {"id": 939719570, "states": "NOTHING", "dates": "2018-06-3002:08:58.425572"},
        {"id": 594226727, "states": "NOTHING", "dates": "2018-09-1221:27:25.241689"},
        {"id": 615064591, "states": "NOTHING", "dates": "2018-10-1408:21:33.419441"},
    ]
