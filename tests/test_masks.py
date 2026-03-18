import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize('number, expected', [
    ("7000792289606361", '7000 79** **** 6361'),
    ("0000000000000000", '0000 00** **** 0000'),
    ("9999999999999999", '9999 99** **** 9999')
])
def test_get_mask_card_number(number, expected):
    assert get_mask_card_number(number) == expected


@pytest.mark.parametrize('number', [
    "999999999999999",
    "00000000000000000",
    ''
])
def test_get_mask_card_number_error(number):
    with pytest.raises(ValueError):
        get_mask_card_number(number)


@pytest.mark.parametrize('number, expected', [
    ('73654108430135874305', '**4305'),
    ('99999999999999999999', '**9999'),
    ('00000000000000000000', '**0000')
])
def test_get_mask_account(number, expected):
    assert get_mask_account(number) == expected


@pytest.mark.parametrize('number', [
    '999999999999999999999',
    '0000000000000000000',
    ''
])
def test_get_mask_account_error(number):
    with pytest.raises(ValueError):
        get_mask_account(number)