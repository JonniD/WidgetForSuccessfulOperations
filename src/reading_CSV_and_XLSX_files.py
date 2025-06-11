import pandas as pd
from typing import Any


def read_CSV(file: str) -> Any:
    '''Функция считывает финансовые операции из CSV файла и возвращает список словарей.'''
    try:
        read_csv = pd.read_csv(file)
        data_transaction = read_csv.to_dict(orient="records")
    except FileNotFoundError:
        data_transaction = []
    return data_transaction


def read_EXCEL(file: str) -> Any:
    '''Функция считывает финансовые операции из XLSX файлов и возвращает список словарей.'''
    try:
        read_xls = pd.read_excel(file)
        data_transaction = read_xls.to_dict(orient="records")
    except FileNotFoundError:
        data_transaction = []
    return data_transaction
