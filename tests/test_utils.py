from src.utils import get_operations_form_json_file


def test_get_operation_form_json_file():
    r = get_operations_form_json_file("data/operations.json")
    assert len(r) == 101
    assert get_operations_form_json_file("data/empty.json") == []
    assert get_operations_form_json_file("data/not_list.json") == []
    assert get_operations_form_json_file("data/not_found.json") == []
