import pytest
from src.widget import mask_account_card, get_date

@pytest.mark.parametrize("account_card, mask", [('Visa Platinum 7000792289606361', 'Visa Platinum 7000 79** **** 6361'),
                                                ('Счет 73654108430135874305', 'Счет **4305'),
                                                ('', 'не корректные данные'),
                                                ('Visa Platinum 700079228960636S', 'не корректные данные'),
                                                ('Счет 7365410843013587430A', 'не корректные данные'),
                                                ('Счет73654108430135874305', 'не корректные данные'),
                                                ('VisaPlatinum7000792289606361', 'не корректные данные'),
                                                ('Счет 7365410843013587430', 'не корректные данные'),
                                                ('Visa Platinum 700079228960636', 'не корректные данные')])
def test_mask_account_card(account_card, mask):
    assert mask_account_card(account_card) == mask


@pytest.mark.parametrize("date_string, date", [("2024-03-11T02:26:18.671407", "11.03.2024"),
                                               ("T02:26:18.671407", 'не корректные данные'),
                                               ("2024-03-1126:18.671407", "11.03.2024")])
def test_get_date(date_string, date):
    assert get_date(date_string) == date
