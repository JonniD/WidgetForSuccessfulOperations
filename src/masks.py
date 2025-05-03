def get_mask_card_number(card_number: str | int) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску."""
    str_card_number = str(card_number).replace(" ", "")
    if len(str_card_number) == 16 and str_card_number.isdigit():
        mask_card_number = f"{str_card_number[:4]} {str_card_number[4:6]}** **** {str_card_number[-4:]}"
        return mask_card_number


def get_mask_account(account: str | int) -> str:
    """Функция принимает на вход номер счета и возвращает его маску."""
    str_account = str(account).replace(" ", "")
    if len(str_account) == 20 and str_account.isdigit():
        mask_account = f"**{str_account[-4:]}"
        return mask_account
