from typing import Iterable


def filter_by_currency(type_transfer: list[dict], value: str | int) -> Iterable[dict]:
    """Генерато,который поочередно выдает транзакции, где валюта операции соответствует заданной"""
    for type_ in type_transfer:
        if type_.get("currency") == str(value):
            yield type_


def transaction_descriptions(info_trans: list[dict]) -> Iterable[str]:
    """Функция генератор, которая возращает описание каждой операции по очереди"""
    for info in info_trans:
        if info.get("description"):
            yield info["description"]


def card_number_generator(start: int | str, end: int | str) -> Iterable[str]:
    """Функиця геенератор, генерирующее номер карты XXXX XXXX XXXX XXXX, итервал, которой мы выбираем"""
    start_int = int(start)
    end_int = int(end)

    if start_int <= 0 or end_int <= 0:
        raise ValueError("Не правильный ввод карты")
    if start_int > end_int:
        raise ValueError

    for number in range(start_int, end_int + 1):
        digits = f"{number:016d}"

        yield f"{digits[:4]} {digits[4:8]} {digits[8:12]} {digits[12:16]}"


if __name__ == "__main__":
    for x in card_number_generator(1, 3):
        print(x)
