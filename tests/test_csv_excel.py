from src.csv_excel import get_operations_form_csv_file, get_operations_form_excel_file


def test_get_operation_form_csv_file() -> None:
    r = get_operations_form_csv_file("data/transactions.csv")
    assert len(r) == 1000
    r = get_operations_form_csv_file("data/transaction.csv")
    assert r == []


def test_get_operation_form_excel_file() -> None:
    r = get_operations_form_excel_file("data/transactions_excel.xlsx")
    assert len(r) == 1000
    r = get_operations_form_excel_file("data/transaction.csv")
    assert r == []
