from src.category_counting import process_bank_operations
from src.csv_excel import get_operations_form_excel_file


def test_category_counting():
    operations = get_operations_form_excel_file("data/transactions_excel.xlsx")
    r = process_bank_operations(operations, ['Перевод организации'])
    assert len(r) > 0