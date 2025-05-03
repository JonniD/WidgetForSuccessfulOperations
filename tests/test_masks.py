from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number(card_number1, card_number2, card_number3, number, empty_string):
    assert get_mask_card_number(card_number1) == "7000 79** **** 6361"
    assert get_mask_card_number(card_number2) == "7000 79** **** 6361"
    assert get_mask_card_number(card_number3) == None
    assert get_mask_card_number(number) == None
    assert get_mask_card_number(empty_string) == None

def test_get_mask_account(account1, account2, account3, number, empty_string):
    assert get_mask_account(account1) == "**4305"
    assert get_mask_account(account2) == "**4305"
    assert get_mask_account(account3) == None
    assert get_mask_account(number) == None
    assert get_mask_account(empty_string) == None
