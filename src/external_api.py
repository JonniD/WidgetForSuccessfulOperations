import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_Key")


def get_rub_transactions(operation: dict[str, Any]) -> Any:
    """
    Возвращает сумму транзакции в рублях.
    :param operation: Входящее значение, словарь с транзакцией.
    :return: Результат в виде числа float или строка с сообщением о возникшей ошибке.
    """
    try:
        code = operation["operationAmount"]["currency"]["code"]
        amount = operation["operationAmount"]["amount"]
    except KeyError as e:
        return f"{e}: Отсутствует значение о сумме операции или валюте."
    if code == "RUB":
        return float(amount)
    else:
        params = {"amount": amount, "to": "RUB", "from": code}
        url = "https://api.apilayer.com/exchangerates_data/convert"
        headers = {
            "apikey": api_key,
        }
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            return response.json().get("result")
        except requests.exceptions.RequestException:
            return "Ошибка обращения к api"
