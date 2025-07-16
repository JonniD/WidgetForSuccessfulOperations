def filter_by_state(list_of_dictionaries: list, state: str = "EXECUTED") -> list | str:
    """
    Функция, которая принимает список словарей и опционально значение для ключа state(по умолчанию 'EXECUTED').
    Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению.
    """
    list_filter_by_state = [d for d in list_of_dictionaries if d.get("state") == state]
    return list_filter_by_state


def sort_by_date(list_of_dictionaries: list, reverse: bool = True) -> list | str:
    """
    Функция, которая принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание).
    Функция возвращает новый список, отсортированный по дате (date)
    """
    if any(d.get("date") for d in list_of_dictionaries):
        return sorted(list_of_dictionaries, key=lambda d: str(d.get("date")), reverse=reverse)
    else:
        return "Некорректные данные"
