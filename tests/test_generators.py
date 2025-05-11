import pytest
import re
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


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


@pytest.mark.parametrize(
    "incorrect_, wrong_",
    [
        ([], []),
        ([
             {
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
                 "from": "Счет 75106830613657916952",
                 "to": "Счет 11776614605963066702"
             }], [])
    ])
def test_transaction_descriptions_non(incorrect_, wrong_):
    result = list(transaction_descriptions(incorrect_))
    assert result == wrong_


def test_card_number_format():
    '''еста для проверки формата номеров карт'''
    start, stop = 4000123456789010, 4000123456789015
    pattern = re.compile(r"\d{4} \d{4} \d{4} \d{4}")
    for card_number in card_number_generator(start, stop):
        assert pattern.match(card_number), f"Неверный формат: {card_number}"


def test_card_number_range():
    '''тестирования генерации номеров в заданном диапазоне'''
    start, stop = 4000123456789010, 4000123456789015
    for card_number in card_number_generator(start, stop):
        card_number_int = int(card_number.replace(' ', ''))
        assert start <= card_number_int <= stop, f"Номер вне диапазона: {card_number}"


def test_card_number_boundaries():
    '''проверку граничных значений '''
    start, stop = 4000123456789010, 4000123456789015
    generated_cards = list(card_number_generator(start, stop))

    # Проверяем, что первый и последний номера равны start и stop
    first_card = int(generated_cards[0].replace(' ', ''))
    last_card = int(generated_cards[-1].replace(' ', ''))

    assert first_card == start, f"Первый номер не равен start: {generated_cards[0]}"
    assert last_card == stop, f"Последний номер не равен stop: {generated_cards[-1]}"
