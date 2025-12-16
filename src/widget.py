from src.masks import get_mask_account
from src.masks import get_mask_card_number


def mask_account_card(info_card_check: str | int) -> str:
    """Возращает маску карты или счета"""
    digits_only = "".join(ch for ch in str(info_card_check).strip() if ch.isdigit())
    if len(digits_only) == 16:
        mask = get_mask_card_number(digits_only)
    elif len(digits_only) == 20:
        mask = get_mask_account(digits_only)
    else:
        return "Не правильный ввод"

    return mask


if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 7000792289606361"))


def get_data(date_str: str | int) -> str:
    """Функция принимает дату делает в формате ДД.ММ.ГГГГ"""
    if len(date_str) > 0:
        filter_date = str(date_str).strip()
        only_date = filter_date.split("T", 1)[0]
        if len(only_date) == 10 or len(only_date) == 8:
            if "-" in only_date:
                year, month, day = only_date.split("-")
                return f"{day}.{month}.{year}"
            else:
                return  "Не правильный ввод даты"


    return "Не правильный ввод даты"


