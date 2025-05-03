import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize(
    "card_number, mask_card_number",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        (7000792289606361, "7000 79** **** 6361"),
        ("7000 7922 8960 6361", "7000 79** **** 6361"),
        ("", "не корректный номер карты"),
        ("7A00792289606361", "не корректный номер карты"),
        ("7000792289606361233", "не корректный номер карты"),
    ],
)
def test_get_mask_card_number(card_number, mask_card_number):
    assert get_mask_card_number(card_number) == mask_card_number


@pytest.mark.parametrize(
    "account, mask_account",
    [
        ("73654108430135874305", "**4305"),
        (73654108430135874305, "**4305"),
        ("7365 4108 4301 3587 4305", "**4305"),
        ("", "не корректный аккаунт"),
        ("73А54108430135874305", "не корректный аккаунт"),
        ("73654108430135874305224", "не корректный аккаунт"),
    ],
)
def test_get_mask_account(account, mask_account):
    assert get_mask_account(account) == mask_account
