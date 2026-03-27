from unittest.mock import Mock, patch

import requests

from src.external_api import get_amount
from src.utils import get_operations_form_json_file


@patch("requests.get")
def test_get_amount(mock_get):
    mock_get.return_value.json.return_value = {"result": 5.5}

    operations = get_operations_form_json_file("data/operations.json")
    get_amount(operations[1])
    mock_get.assert_called_once()


def test_get_amount_case_two():
    mock_get = Mock()
    requests.get = mock_get
    mock_get.return_value.json.return_value = {"result": 5.5}

    operations = get_operations_form_json_file("data/operations.json")
    get_amount(operations[2])
    mock_get.assert_called_once()
