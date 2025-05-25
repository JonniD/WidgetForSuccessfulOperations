import json
from unittest.mock import mock_open, patch

from src.utils import getting_financial_transaction_data


def test_getting_financial_transaction_data_correct(json_example: list[dict[str, str | int]]) -> None:
    with patch("builtins.open", mock_open(read_data=json.dumps(json_example))) as mock_file:
        assert getting_financial_transaction_data("builtins.open") == json_example
        mock_file.assert_called_once_with("builtins.open", "r", encoding="utf-8")


def test_getting_financial_transaction_data_error(wrong_json_list: list[dict[str, str | int]]) -> None:
    with patch("builtins.open", mock_open(read_data=str(wrong_json_list))) as mock_file:
        assert getting_financial_transaction_data("builtins.open") == []
        mock_file.assert_called_once_with("builtins.open", "r", encoding="utf-8")


def test_getting_financial_transaction_data_no_file() -> None:
    assert getting_financial_transaction_data("wrong_path") == []
