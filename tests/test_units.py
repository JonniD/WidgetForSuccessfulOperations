import json
from unittest import mock
from unittest.mock import patch, mock_open

import pytest

from src.units import getting_financial_transaction_data



# проверяем код на положительный исход
def test_get_transactions_correct(correct_path: list[dict[str, str | int]]) -> None:
    with patch("builtins.open", mock_open(read_data=json.dumps(correct_path))) as mock_file:
        assert getting_financial_transaction_data("builtins.open") == correct_path
        mock_file.assert_called_once_with("builtins.open", "r", encoding="utf-8")



@mock.patch('builtins.open', side_effect=FileNotFoundError)
def test_file_not_found(mock_open):
    result = getting_financial_transaction_data('fake_path.json')
    assert result == []


@mock.patch('json.load', side_effect=json.JSONDecodeError("Expecting value", "", 0))
def test_json_decode_error(mock_json_load):
    result = getting_financial_transaction_data('fake_path.json')
    assert result == []
