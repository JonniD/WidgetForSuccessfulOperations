from src.widget import mask_account_card, get_date


def test_mask_account_card(card_number1, card_number2, card_number3, account1, account2, account3, number,
                           empty_string):
    assert mask_account_card(card_number1) == '7000 79** **** 6361'
    assert mask_account_card(card_number2) == '7000 79** **** 6361'
    assert mask_account_card(card_number3) == None
    assert get_mask_account(account1) == '**4305'
    assert get_mask_account(account2) == '**4305'
    assert get_mask_account(account3) == None
    assert get_mask_account(number) == None
    assert get_mask_account(empty_string) == None
