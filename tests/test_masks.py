from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number():
    assert get_mask_card_number(7000792289606361) == '7000 79** **** 6361'
    assert get_mask_card_number('7000792289606361') == '7000 79** **** 6361'
    assert get_mask_card_number('7B00792289606361') == None
    assert get_mask_card_number(11111123) == None
    assert get_mask_card_number("") == None

def test_get_mask_account():
    assert get_mask_account(7000792289606361) == '7000 79** **** 6361'
    assert get_mask_account('7000792289606361') == '7000 79** **** 6361'
    assert get_mask_account('7B00792289606361') == None
    assert get_mask_account(11111123) == None
    assert get_mask_account("") == None