import pytest
from src.processing import filter_by_state, sort_by_date

wrong_account_card = "Некорректные данные"
BANKING_OPERATIONS = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def test_filter_by_state_and_sort_by_date_correct(processing_data: list[dict[str, str | int]]) -> None:
    """
    Тестируем функции filter_by_state и sort_by_date с использованием корректных данных.
    """
    assert filter_by_state(processing_data) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}
    ]
    assert filter_by_state(processing_data, "CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}
    ]
    assert sort_by_date(processing_data) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    assert sort_by_date(processing_data, False) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}
    ]
    assert sort_by_date(processing_data, '') == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}
    ]
    assert sort_by_date(processing_data, ' ') == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    assert sort_by_date(processing_data, None) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}
    ]


@pytest.mark.parametrize(
    "data, arg, expected",
    [
        (
                BANKING_OPERATIONS,
                "RANDOM TEXT",
                wrong_account_card,
        ),
        (
                BANKING_OPERATIONS,
                None,
                wrong_account_card,
        ),
        (
                BANKING_OPERATIONS,
                "",
                wrong_account_card,
        ),
    ],
)
def test_filter_params_incorrect(data: list[dict[str, str | int]], arg: str,
                                 expected: list[dict[str, str | int]]) -> None:
    """
    Тестируем функцию filter_by_state с использованием некорректных аргументов.
    """
    assert filter_by_state(data, arg) == expected


def test_filter_and_sorting_wrong(processing_data_wrong: list[dict[str, str | int]]) -> None:
    """
    Тестируем функции filter_by_state и sort_by_date с использованием некорректных данных.
    """
    assert filter_by_state(processing_data_wrong) == wrong_account_card
    assert sort_by_date(processing_data_wrong) == wrong_account_card
    assert filter_by_state([]) == wrong_account_card
    assert sort_by_date([]) == wrong_account_card
