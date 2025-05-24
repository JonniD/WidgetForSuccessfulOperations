import json

from src.external_api import get_rub_transactions


def getting_financial_transaction_data(path_to_file: str) -> list[dict]:
    """Функция принимает путь к файлу с транзакциями и возвращает их"""
    try:
        with open(path_to_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print("Файл не найден")
        return []
    except json.JSONDecodeError:
        print("Ошибка декодирования файла")
        return []


