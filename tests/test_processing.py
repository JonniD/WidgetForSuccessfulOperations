from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(list_of_dic, list_of_EXECUTED, list_of_CANCELED):
    assert filter_by_state(list_of_dic, 'EXECUTED') == list_of_EXECUTED
    assert filter_by_state(list_of_dic, 'CANCELED') == list_of_CANCELED
    assert filter_by_state(list_of_dic) == list_of_EXECUTED
