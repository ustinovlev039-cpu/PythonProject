from src.masks import get_mask_account
from src.masks import get_mask_card_number


def mask_account_card(info_card_check: str | int) -> str:
    """Возращает маску карты или счета"""
    digits_only = "".join(ch for ch in str(info_card_check) if ch.isdigit())
    if len(digits_only) == 16:
        mask = get_mask_card_number(digits_only)
    else:
        mask = get_mask_account(digits_only)

    return mask


if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 7000792289606361"))


def get_data(date_str: str) -> str:
    """Функция принимает дату делает в формате ДД.ММ.ГГГГ"""
    only_date = date_str.split("T", 1)[0]
    year, month, day = only_date.split("-")
    return f"{day}.{month}.{year}"


if __name__ == "__main__":
    print(get_data("2024-03-11T02:26:18.671407"))
