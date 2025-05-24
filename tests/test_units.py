import json
from unittest.mock import mock_open, patch

from src.units import getting_financial_transaction_data


def test_get_transactions_correct(json_sample: list[dict[str, str | int]]) -> None:
    with patch("builtins.open", mock_open(read_data=json.dumps(json_sample))) as mock_file:
        assert getting_financial_transaction_data("builtins.open") == json_sample
        mock_file.assert_called_once_with("builtins.open", "r", encoding="utf-8")


def test_get_transactions_decode_error(wrong_json_list: list[dict[str, str | int]]) -> None:
    with patch("builtins.open", mock_open(read_data=str(wrong_json_list))) as mock_file:
        assert getting_financial_transaction_data("builtins.open") == []
        mock_file.assert_called_once_with("builtins.open", "r", encoding="utf-8")


def test_get_transactions_no_file() -> None:
    assert getting_financial_transaction_data("wrong_path") == []