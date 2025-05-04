from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(account_card: str) -> str:
    """Функция, которая умеет обрабатывать информацию как о картах и счетах."""
    account_card_list = account_card.split()
    if len(account_card) == 0 or len(account_card_list) < 2 or not account_card_list[-1].isdigit():
        return "Некорректный номер карты или счета"
    if (account_card_list[0] == "Счет" or account_card_list[0] == 'Счёт') and len(account_card_list[-1]) == 20:
        return f"{account_card_list[0]} {get_mask_account(account_card_list[-1])}"
    else:
        if len(account_card_list[-1]) == 16 and (account_card_list[0] != "Счет" or account_card_list[0] != 'Счёт'):
            mask_card = []
            for element in account_card_list:
                if not element.isdigit():
                    mask_card.append(element)
                else:
                    mask_card.append(get_mask_card_number(element))
            return " ".join(mask_card)
        else:
            return "Некорректный номер карты или счета"


def get_date(date_and_time: str) -> str:
    """
    Функция, которая принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ"
    """
    if len(date_and_time) == 26 and date_and_time[4] == '-' and date_and_time[7] == '-':
        date_list = date_and_time.split("-")
        date = f"{date_list[2][:2]}.{date_list[1]}.{date_list[0]}"
        return date
    else:
        return "Некорректный формат даты."