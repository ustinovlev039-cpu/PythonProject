import pytest
from src.widget import mask_account_card
from src.widget import get_data

@pytest.mark.parametrize("card_or_number, mask_card_or_number", [
    ("Maestro 1596837868705199", "1596 83** *****5199"),
    ("MasterCard 7158300734726758", "7158 30** *****6758"),
    ("Visa Platinum 8990922113665229", "8990 92** *****5229"),
    ("Счет 64686473678894779589", "**9589"),
    ("Счет 35383033474447895560", "**5560"),
    ("Счет 73654108430135874305", "**4305"),
    (73654108430135874305, "**4305"),
    (8990922113665229, "8990 92** *****5229"),
    ("     Visa Platinum 8990922113665229", "8990 92** *****5229"),
    ("Visa 8990922113665229", "8990 92** *****5229"),
    (" ", "Не правильный ввод"),
    ("", "Не правильный ввод"),
    ("Maestro 159683786870519913142", "Не правильный ввод"),
    ("Maestro 159683786870519913142wvjciwevfw9wp", "Не правильный ввод"),
    ("Счет 73654108430135874305ivhwicv9c", "Не правильный ввод"),
    ("Счет 73654108430135874305219373129842", "Не правильный ввод")
])

def test_mask_account_card(card_or_number, mask_card_or_number):
    assert mask_account_card(card_or_number) == mask_card_or_number



@pytest.mark.parametrize("data_str, result_data", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2019-07-03T18:35:29.512364", "03.07.2019"),
    ("2018-06-30T02:08:58.425572", "30.06.2018"),
    ("20180630T02:08:58.425572", "30.06.2018"),
    #("2018-06-30T02:08:58.425572", "30.06.2018")


])

def test_get_data(data_str, result_data):
    assert get_data(data_str) == result_data
