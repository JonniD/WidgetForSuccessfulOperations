import json
from typing import Any
import logging

logger = logging.getLogger('utils')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('../logs/utils.log', mode='w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def getting_financial_transaction_data(path_to_file: str) -> Any:
    """Функция принимает путь к файлу с транзакциями и возвращает их"""
    try:
        with open(path_to_file, "r", encoding="utf-8") as f:
            logger.info(f"Файл успешно прочитан")
            data = json.load(f)
            logger.info("Транзакции обработаны")
            return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"В работе функции возникла ошибка {e}")
        return []
