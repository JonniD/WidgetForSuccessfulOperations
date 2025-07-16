import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Функцию, которая принимает список словарей с данными о банковских операциях и строку поиска,
    возвращает список словарей, у которых в описании есть данная строка."""
    pattern = re.compile(re.escape(search), re.IGNORECASE)
    result = []
    for record in data:
        description = record.get("description", "")
        if pattern.search(description):
            result.append(record)
    return result


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Функцию, которая принимает список словарей с данными о банковских операциях и список категорий операций,
    возвращать словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой категории.
    Категории операций хранятся в поле description.
    """
    counter = Counter()
    for record in data:
        description = record.get("description", "")
        for category in categories:
            if category.lower() in description.lower():
                counter[category] += 1
                break
    return dict(counter)
