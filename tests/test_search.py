from src.search import process_bank_search
from src.csv_excel import get_operations_form_excel_file


def test_process_bank_search() -> None:
    operations = get_operations_form_excel_file("data/transactions_excel.xlsx")
    print('operations:', len(operations))
    r = process_bank_search(operations, 'Перевод организации')
    assert len(r) > 0