from typing import Any


from unittest.mock import patch

import pytest

from src.external_api import get_rub_transactions



def test_get_rub_transactions(rub_conversion) -> None:
    assert get_rub_transactions(rub_conversion) == 31957.58


@patch('requests.get')
def test_get_rub_transactions_usd(mock_get, usd_conversion) -> None:
    mock_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 8221.37},
        "info": {"timestamp": 1747777395, "rate": 80.624798},
        "date": "2025-05-20",
        "result": 662846.295533,
    }
    assert get_rub_transactions(usd_conversion) == 662846.295533
    mock_get.assert_called_once()

@patch('requests.get')
def test_get_rub_transactions_eur(mock_get, eur_conversion) -> None:
    mock_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "EUR", "to": "RUB", "amount": 9824.07},
        "info": {"timestamp": 1747791437, "rate": 91.000365},
        "date": "2025-05-21",
        "result": 893993.955786,
    }
    assert get_rub_transactions(eur_conversion) == 893993.955786
    mock_get.assert_called_once()


@patch('requests.get')
def test_get_rub_transactions_err(mock_get, incorrect_conversion: dict[str, Any]) -> None:
    mock_get.return_value.json.return_value = {"result": "Ошибка обращения к api"}
    assert get_rub_transactions(incorrect_conversion) == "Ошибка обращения к api"
    mock_get.assert_called_once()

@pytest.mark.parametrize(
    "operation, expected",
    [
        ({}, "'operationAmount': Отсутствует значение о сумме операции или валюте."),
        (
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "31957.58", "currency": {"name": "руб."}},
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
            },
            "'code': Отсутствует значение о сумме операции или валюте.",
        ),
    ],
)
def test_get_rub_transactions(operation: dict[str, Any], expected: str) -> None:
    assert get_rub_transactions(operation) == expected