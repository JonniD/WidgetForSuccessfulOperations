import pytest

from src.masks import get_mask_account, get_mask_card_number

wrong_number_card = "некорректный номер карты, номер должен состоять из 16 цифр без дополнительных символов и букв"
wrong_number_account = "некорректный аккаунт, аккаунт должен состоять из 20 цифр без дополнительных символов и букв"


def test_get_mask_card_number_correct(card_number: str) -> None:
    """Тест функции get_mask_card_number с использованием корректных данных"""
    assert get_mask_card_number(card_number) == "7000 79** **** 6361"


@pytest.mark.parametrize(
    "incorrect_card_number, wrong_number",
    [
        ("", wrong_number_card),
        ("123456789012345", wrong_number_card),
        ("12345678901234567", wrong_number_card),
        ("7000 7922 8960 6361", wrong_number_card),
        ("7000-7922-8960-6361", wrong_number_card),
        ("Card 7000792289606361", wrong_number_card),
        ("Card № 7000792289606361", wrong_number_card),
        ("123456789012345A", wrong_number_card),
        ("Number Card", wrong_number_card),
    ],
)
def test_get_mask_card_number(incorrect_card_number: str, wrong_number: str) -> None:
    """Тест функции get_mask_card_number с использованием некорректных данных"""
    assert get_mask_card_number(incorrect_card_number) == wrong_number


def test_get_mask_account_correct(account: str) -> None:
    """Тест функции get_mask_account с использованием корректных данных"""
    assert get_mask_account(account) == "**4305"


@pytest.mark.parametrize(
    "incorrect_account, wrong_account",
    [
        ("", wrong_number_account),
        ("1234567890123456789", wrong_number_account),
        ("123456789012345678901", wrong_number_account),
        ("7365 4108 4301 3587 4305", wrong_number_account),
        ("73А54108430135874305", wrong_number_account),
        ("7365-4108-4301-3587-4305", wrong_number_account),
        ("Account 73654108430135874305", wrong_number_account),
        ("Счет номер", wrong_number_account),
    ],
)
def test_get_mask_account(incorrect_account: str, wrong_account: str):
    """Тест функции get_mask_account с использованием некорректных данных"""
    assert get_mask_account(incorrect_account) == wrong_account
