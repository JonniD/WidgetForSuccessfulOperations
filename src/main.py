import os
import time

from config import ROOT_DIR
from src.filter_operations import process_bank_search
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.reading_csv_and_xlsx_files import read_CSV, read_EXCEL
from src.utils import getting_financial_transaction_data
from src.widget import get_date, mask_account_card

path_to_data = os.path.join(ROOT_DIR, "data")

path_to_json = os.path.join(path_to_data, "operations.json")
path_to_csv = os.path.join(path_to_data, "transactions.csv")
path_to_xls = os.path.join(path_to_data, "transactions_excel.xlsx")


def main() -> str:
    """
    Основная логика программы.
    Собирает воедино основной функционал и предоставляет пользователю удобную функцию поиска и вывода транзакций.
    Выводит сообщение об успешной отработке программы.
    """
    print(
        """Привет! Добро пожаловать в программу работы
с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла"""
    )
    user_format = input()
    while user_format not in ("1", "2", "3"):
        user_format = input("Выберите подходящий пункт из меню")
    if user_format == "1":
        transactions = getting_financial_transaction_data(path_to_json)
        print(transactions)
        print("Для обработки выбран JSON-файл.")
    elif user_format == "2":
        transactions = read_CSV(path_to_csv)
        print(transactions)
        print("Для обработки выбран CSV-файл.")
    else:
        transactions = read_EXCEL(path_to_xls)
        print(transactions)
        print("Для обработки выбран XLSX-файл.")

    print(
        """Программа: Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
    )
    user_status = input().upper()
    while user_status not in ("EXECUTED", "CANCELED", "PENDING"):
        user_status = input(
            f"""Статус операции {user_status} недоступен.
Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
"""
        ).upper()
    filtered_transactions = filter_by_state(transactions, user_status)
    print("Отсортировать операции по дате? Да/Нет")
    sort_choice = input().lower()
    while sort_choice not in ("да", "нет"):
        sort_choice = input('Введите "ДА" или "НЕТ" для выбора варианта\n').lower()
    if sort_choice == "да":
        print("Отсортировать по возрастанию или по убыванию?")
        sort_settings = input().lower()
        while sort_settings not in ("по возрастанию", "по убыванию"):
            sort_settings = input('Выберите порядок сортировки "по убыванию"/"по возрастанию"').lower()
        if sort_settings == "по возрастанию":
            filtered_transactions = sort_by_date(filtered_transactions, False)
        else:
            filtered_transactions = sort_by_date(filtered_transactions)
    print("Выводить только рублевые транзакции? Да/Нет")
    rub_option = input().lower()
    while rub_option not in ("да", "нет"):
        rub_option = input('Введите "ДА" или "НЕТ" для выбора варианта').lower()
    if rub_option == "да":
        filtered_transactions = list(filter_by_currency(filtered_transactions, "RUB"))
    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    filter_choice = input().lower()
    while filter_choice not in ("да", "нет"):
        filter_choice = input('Введите "ДА" или "НЕТ" для выбора варианта').lower()
    if filter_choice == "да":
        print("Введите ключевое слово для фильтрации")
        keyword = input().lower()
        filtered_transactions = process_bank_search(filtered_transactions, keyword)
    print("Распечатываю итоговый список транзакций", end="", flush=True)
    for i in range(3):
        time.sleep(1)
        print(".", end="", flush=True)
    print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
    if len(filtered_transactions) != 0:
        for transaction in filtered_transactions:
            from_v = transaction.get("from")
            to_v = transaction.get("to")
            description = transaction.get("description")
            amount_json = transaction.get("operationAmount", {}).get("amount")
            curr_json = transaction.get("operationAmount", {}).get("currency", {}).get("name")
            amount = transaction.get("amount")
            curr = "руб." if transaction.get("currency_name") == "Ruble" else transaction.get("currency_name")
            date = transaction.get("date")
            if amount_json is None and description == "Открытие вклада":
                result = f"{get_date(date)} {description}\n" f"{mask_account_card(to_v)}\n" f"Сумма: {amount} {curr}\n"
                print(result)
            elif amount_json is None and description != "Открытие вклада":
                result = (
                    f"{get_date(date)} {description}\n"
                    f"{mask_account_card(from_v)} -> {mask_account_card(to_v)}\n"
                    f"Сумма: {amount} {curr}\n"
                )
                print(result)
            elif amount_json is not None and description == "Открытие вклада":
                result = (
                    f"{get_date(date)} {description}\n"
                    f"{mask_account_card(to_v)}\n"
                    f"Сумма: {amount_json} {curr_json}\n"
                )
                print(result)
            elif amount_json is not None and description != "Открытие вклада":
                result = (
                    f"{get_date(date)} {description}\n"
                    f"{mask_account_card(from_v)} -> {mask_account_card(to_v)}\n"
                    f"Сумма: {amount_json} {curr_json}\n"
                )
                print(result)
            else:
                return "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    return "Завершение работы программы."


print(main())
