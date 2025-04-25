def filter_by_state(list_of_dictionaries: list, state: str = "EXECUTED") -> list:
    list_filter_by_state = []
    for dictionary in list_of_dictionaries:
        if dictionary['state'] == state:
            list_filter_by_state.append(dictionary)
    return list_filter_by_state


def sort_by_date(list_of_dictionaries: list, reverse: bool = True) -> list:
    return sorted(list_of_dictionaries, key=lambda x: x["date"], reverse=reverse)


list_dictionaries = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
stat = 'CANCELED'
print(sort_by_date(list_dictionaries))
