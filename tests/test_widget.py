from src.widget import mask_account_card


def test_mask_account_card(
    card_number1, card_number2, card_number3, account1, account2, account3, number, empty_string
):
    assert mask_account_card(card_number1) == "7000 79** **** 6361"
    assert mask_account_card(card_number2) == "7000 79** **** 6361"
    assert mask_account_card(card_number3) == None
    assert mask_account_card(account1) == "**4305"
    assert mask_account_card(account2) == "**4305"
    assert mask_account_card(account3) == None
    assert mask_account_card(number) == None
    assert mask_account_card(empty_string) == None
