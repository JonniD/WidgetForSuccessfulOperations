from src.widget import mask_account_card, get_date


def test_mask_account_card(card1, card2, card3, empty_string, account1, account2):
    assert mask_account_card(card1) == "Maestro 1596 83** **** 5199"
    assert mask_account_card(card2) == 'Visa Classic 6831 98** **** 7658'
    assert mask_account_card(card3) == "MasterCard 7158 30** **** 6758"
    assert mask_account_card(empty_string) == None
    assert mask_account_card(account1) == "Счет **9589"
    assert mask_account_card(account2) == "Счет **5560"


def test_get_date(date, empty_string):
    assert get_date(date) == "11.03.2024"
    assert get_date(empty_string) == None
