from masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Функция, которая умеет обрабатывать информацию как о картах и счетах."""
    account_card_list = account_card.split()
    if account_card_list[0] == "Счет":
        return f"Счет {get_mask_account(account_card_list[1])}"
    else:
        mask_card = []
        for element in account_card_list:
            if not element.isdigit():
                mask_card.append(element)
            else:
                mask_card.append(get_mask_card_number(element))
        return " ".join(mask_card)


def get_date(date_and_time: str) -> str:
    """
    Функция, которая принимает на вход строку
    с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ"
    """
    date_list = date_and_time.split("-")
    date = f"{date_list[2][:2]}.{date_list[1]}.{date_list[0]}"
    return date
