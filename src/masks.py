import logging

logger = logging.getLogger('masks')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('../logs/masks.log',mode='w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску."""
    logger.info(f'Проверяем корректность номера карты')
    if len(card_number) != 16 or not card_number.isdigit():
        return "некорректный номер карты, номер должен состоять из 16 цифр без дополнительных символов и букв"
    logger.info("маскируем номер карты")
    mask_card_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return mask_card_number


def get_mask_account(account: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску."""
    logger.info(f'Проверяем корректность номера счета')
    if len(account) != 20 or not account.isdigit():
        return "некорректный аккаунт, аккаунт должен состоять из 20 цифр без дополнительных символов и букв"
    logger.info("маскируем номер счета")
    mask_account = f"**{account[-4:]}"
    return mask_account
