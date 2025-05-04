def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску."""
    if len(card_number) != 16 or not card_number.isdigit():
        return "некорректный номер карты, номер должен состоять из 16 цифр без дополнительных символов и букв"
    mask_card_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return mask_card_number


def get_mask_account(account: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску."""
    if len(account) != 20 or not account.isdigit():
        return "некорректный аккаунт, аккаунт должен состоять из 20 цифр без дополнительных символов и букв"
    mask_account = f"**{account[-4:]}"
    return mask_account
