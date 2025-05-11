def filter_by_currency(all_transactions: list[dict[str, str | int]], name_currency: str):
    """Функция filter_by_currency, которая принимает на вход список словарей, представляющих транзакции.
    Функция возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной"""
    for transaction in all_transactions:
        if transaction["operationAmount"]["currency"]["name"] == name_currency:
            yield transaction


def transaction_descriptions(transactions: list[dict[str, str | int]]):
    """генератор transaction_descriptions, который принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди."""
    for transaction in transactions:
        if "description" in transaction:
            yield transaction["description"]


def card_number_generator(start: int, end: int):
    """генератор card_number_generator, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX,
    где X — цифра номера карты.
     Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999."""
    for num in range(start, end + 1):
        str_num = f"{num:016}"
        yield f"{str_num[:4]} {str_num[4:8]} {str_num[8:12]} {str_num[12:]}"
