import pytest

from src.generators import filter_by_currency, transaction_descriptions


def test_filter_by_currency_correct_USD(transactions):
    usd_transactions = filter_by_currency(transactions, "USD")
    list_result = []
    for _ in range(2):
        list_result.append(next(usd_transactions))
    assert list_result == [{
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    }, {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    }]


def test_filter_by_currency_correct_RUB(transactions):
    usd_transactions = filter_by_currency(transactions, "руб.")
    list_result = []
    for _ in range(2):
        list_result.append(next(usd_transactions))
    assert list_result == [{
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {
            "amount": "43318.34",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160"
    }, {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {
            "amount": "67314.70",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657"
    }]


def test_filter_by_currency_correct_none():
    result = list(filter_by_currency([], "USD"))
    assert result == []


def test_filter_by_currency_correct_EU(transactions):
    result = list(filter_by_currency(transactions, "EU"))
    assert result == []


def test_transaction_descriptions_USD(transactions):
    descriptions = transaction_descriptions(transactions)
    list_result = []
    for _ in range(5):
        list_result.append(next(descriptions))
    assert list_result == ['Перевод организации', 'Перевод со счета на счет',
                           'Перевод со счета на счет', 'Перевод с карты на карту', 'Перевод организации']


def test_transaction_descriptions_non():
    result = list(transaction_descriptions([]))
    assert result == []
