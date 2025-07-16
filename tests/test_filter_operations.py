from src.filter_operations import process_bank_search,process_bank_operations


def test_process_bank_search(json_sample: list[dict[str, str | int]], maestro: list[dict[str, str | int]]) -> None:
    assert process_bank_search(json_sample, keyword="перевод") == json_sample
    assert process_bank_search(json_sample, keyword="слово") == json_sample
    assert process_bank_search(json_sample, keyword="Maestro") == maestro


def test_process_bank_operations(json_sample: list[dict[str, str | int]], categories: list[str]) -> None:
    assert process_bank_operations(json_sample, categories) == {"Перевод организации": 3}
    assert process_bank_operations(json_sample, []) == {}