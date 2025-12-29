import pytest

from src.masks import get_mask_account
from src.masks import get_mask_card_number


@pytest.mark.parametrize(
    "card, mask_card",
    [
        ("1596837868705199", "1596 83** *****5199"),
        ("7158300734726758", "7158 30** *****6758"),
        ("8990922113665229", "8990 92** *****5229"),
        ("133545686457797646787", "Не правильный ввод карты"),
        (1596837868705199, "1596 83** *****5199"),
        ("    8990922113665229", "8990 92** *****5229"),
        ("8990922113665229        ", "8990 92** *****5229"),
        (" ", "Не правильный ввод карты"),
        ("", "Не правильный ввод карты"),
    ],
)
def test_get_mask_card_number(card, mask_card):
    assert get_mask_card_number(card) == mask_card


@pytest.mark.parametrize(
    "numbers, numbers_mask",
    [
        ("35383033474447895560", "**5560"),
        ("73654108430135874305", "**4305"),
        (73654108430135874305, "**4305"),
        ("       73654108430135874305", "**4305"),
        ("73654108430135874305132141", "Не правильный ввод счета"),
        ("36541084301358743", "Не правильный ввод счета"),
    ],
)
def test_get_mask_account(numbers, numbers_mask):
    assert get_mask_account(numbers) == numbers_mask
