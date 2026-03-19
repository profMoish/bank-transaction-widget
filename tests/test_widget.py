from datetime import datetime
import pytest

from src.widget import mask_account_card, get_data

@pytest.mark.parametrize('number, expected', [
    ('Visa Platinum 7000792289606361', 'Visa Platinum 7000 79** **** 6361'),
    ('Maestro 7000792289606361', 'Maestro 7000 79** **** 6361'),
    ('Счет 73654108430135874305', 'Счет **4305'),
    ('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
    ('Счет 64686473678894779589', 'Счет **9589'),
    ('MasterCard 7158300734726758', 'MasterCard 7158 30** **** 6758'),
    ('Счет 35383033474447895560', 'Счет **5560'),
    ('Visa Classic 6831982476737658', 'Visa Classic 6831 98** **** 7658'),
    ('Visa Platinum 8990922113665229', 'Visa Platinum 8990 92** **** 5229'),
    ('Visa Gold 5999414228426353', 'Visa Gold 5999 41** **** 6353'),
    ('Счет 73654108430135874305', 'Счет **4305')
])
def test_mask_account_card(number, expected):
    assert mask_account_card(number) == expected

@pytest.mark.parametrize('number', [
    'Maestro 70007922896063600',
    'Счет73654108430135874305',
    'Счет 1 73654108430135874305',
    'Счет 7365410843013587430a',
    'СчетСчетСчетСчет',
    'Счет',
    '',
])
def test_error_mask_account_card(number):
    with pytest.raises(ValueError) as e:
        mask_account_card(number)
    print(e.value)



@pytest.mark.parametrize('date, expected', [
    ('2024-03-11T02:26:18.671407', datetime(2024, 3, 11, 2, 26, 18, 671407)),
])
def test_get_data(date, expected):
    assert get_data(date) == expected

@pytest.mark.parametrize('date', [
    '2024-03-12',
    '2024/03/12',
    ''
])
def test_error_get_data(date):
    with pytest.raises(ValueError):
        get_data(date)