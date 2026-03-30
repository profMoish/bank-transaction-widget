from unittest.mock import Mock, patch
import pandas as pd

from src.csv_excel import get_operations_form_csv_file, get_operations_form_excel_file


def test_get_operation_form_csv_file() -> None:
    r = get_operations_form_csv_file("data/transactions.csv")
    assert len(r) == 1000
    r = get_operations_form_csv_file("data/transaction.csv")
    assert r == []


def test_get_operation_form_csv_file_with_patch() -> None:
    with patch("pandas.read_csv") as mock_read_csv:
        mock_read_csv.return_value.to_dict.return_value = [{"col1": 1, "col2": 2}]
        r = get_operations_form_csv_file("data/transactions.csv")
        assert len(r) == 1
        mock_read_csv.assert_called_once()


def test_get_operation_form_excel_file() -> None:
    r = get_operations_form_excel_file("data/transactions_excel.xlsx")
    assert len(r) == 1000
    r = get_operations_form_excel_file("data/transaction.xlsx")
    assert r == []


def test_get_operation_form_excel_file_with_mock() -> None:
    mock_read_csv = Mock()
    pd.read_csv = mock_read_csv
    mock_read_csv.return_value.to_dict.return_value = [{"col1": 1, "col2": 2}]
    r = get_operations_form_csv_file("data/transactions.csv")
    assert len(r) == 1
    mock_read_csv.assert_called_once()