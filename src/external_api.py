import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()
api_token = os.getenv("API_TOKEN")
api_url = os.getenv("API_URL")


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
        url = api_url
        headers = {
            "apikey": api_token,
        }
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            return response.json().get("result")
        except requests.exceptions.RequestException:
            return "Ошибка обращения к api"


L