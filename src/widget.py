# from src.masks import get_mask_account
# from src.masks import get_mask_card_number
#
#
# def mask_account_card(info_card_check: str | int) -> str:
#     """Возращает маску карты или счета"""
#     digits_only = "".join(ch for ch in str(info_card_check).strip() if ch.isdigit())
#     if len(digits_only) == 16:
#         mask = get_mask_card_number(digits_only)
#     elif len(digits_only) == 20:
#         mask = get_mask_account(digits_only)
#     else:
#         return "Не правильный ввод"
#
#     return mask
#
#
# if __name__ == "__main__":
#     print(mask_account_card("Visa Platinum 7000792289606361"))
#
#
# def get_data(date_str: str) -> str:
#     """Функция принимает дату делает в формате ДД.ММ.ГГГГ"""
#     only_date = date_str.split("T", 1)[0]
#     if len(only_date) == 10 or len(only_date) == 8:
#         if only_date in "-":
#             year, month, day = only_date.split("-")
#             return f"{day}.{month}.{year}"
#         else:
#             result = only_da
#
#
# if __name__ == "__main__":
#     print(get_data("2024-03-11T02:26:18.671407"))



result = "20240311"
print(result.split())