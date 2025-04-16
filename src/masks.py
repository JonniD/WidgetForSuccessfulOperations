def get_mask_card_number(card_number: str | int) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску."""
    str_card_number = str(card_number).replace(" ", "")
    mask_card_number = f"{str_card_number[:4]} {str_card_number[4:6]}** **** {str_card_number[-4:]}"
    return mask_card_number


def get_mask_account(account: str | int) -> str:
    """Функция принимает на вход номер счета и возвращает его маску."""
    str_account = str(account).replace(" ", "")
    mask_account = f"**{str_account[-4:]}"
    return mask_account
