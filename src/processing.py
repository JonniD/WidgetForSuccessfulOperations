def filter_by_state(list_of_dictionaries: list, state: str = "EXECUTED") -> list:
    """
    Функция, которая принимает список словарей и опционально значение для ключа state(по умолчанию 'EXECUTED').
    Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению.
    """
    list_filter_by_state = []
    for dictionary in list_of_dictionaries:
        if dictionary["state"] == state:
            list_filter_by_state.append(dictionary)
    return list_filter_by_state


def sort_by_date(list_of_dictionaries: list, reverse: bool = True) -> list:
    """
    Функция, которая принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание).
    Функция возвращает новый список, отсортированный по дате (date)
    """
    return sorted(list_of_dictionaries, key=lambda x: x["date"], reverse=reverse)
