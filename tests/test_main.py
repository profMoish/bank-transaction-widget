from unittest.mock import patch

import pytest

from src.main import main

# def test_main():
#     main()


@pytest.mark.parametrize(
    "inputs, expected_file, expected_status, return_count",
    [
        (["1", "EXECUTED", "да", "по возрастанию", "нет", "да", "Перевод организации"], "JSON-файл", "EXECUTED", 33),
        (["2", "canceled", "да", "По убыванию", "нет", "да", "Открытие вклада"], "CSV-файл", "CANCELED", 18),
        (["3", "PENDING", "нет", "нет", "нет"], "XLSX-файл", "PENDING", 146),
    ],
)
def test_main_file_and_status(inputs, expected_file, expected_status, return_count, capsys):
    with patch("builtins.input", side_effect=inputs):
        main()
    captured = capsys.readouterr()
    assert expected_file in captured.out
    assert f"Операции отфильтрованы по статусу {expected_status}" in captured.out
    assert f"Всего банковских операций в выборке: {return_count}" in captured.out


def test_main_invalid_status_then_valid(capsys):
    with patch("builtins.input", side_effect=["1", "UNKNOWN", "EXECUTED", "нет", "нет", "нет"]):
        main()
    captured = capsys.readouterr()
    assert 'UNKNOWN" недоступен' in captured.out
    assert "Операции отфильтрованы по статусу EXECUTED" in captured.out


def test_main_multiple_invalid_statuses(capsys):
    with patch("builtins.input", side_effect=["1", "BAD", "WRONG", "PENDING", "нет", "нет", "нет"]):
        main()
    captured = capsys.readouterr()
    assert captured.out.count("недоступен") == 2
    assert "Операции отфильтрованы по статусу PENDING" in captured.out
