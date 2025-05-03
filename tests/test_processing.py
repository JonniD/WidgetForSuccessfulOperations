from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(list_of_dic, list_of_EXECUTED, list_of_CANCELED):
    assert filter_by_state(list_of_dic, "EXECUTED") == list_of_EXECUTED
    assert filter_by_state(list_of_dic, "CANCELED") == list_of_CANCELED
    assert filter_by_state(list_of_dic) == list_of_EXECUTED


def test_sort_by_date(date, sort_date, the_same_date):
    assert sort_by_date(date) == sort_date
    assert sort_by_date(date, False) == sort_date[::-1]
    assert sort_by_date(the_same_date) == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                           {'id': 594226727, 'state': 'CANCELED', 'date': '2018-10-14T21:27:25.241689'},
                                           {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                                           {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
