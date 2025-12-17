from typing import Iterable


def filter_by_currency(info_transfer: list[dict], value: str | int) -> Iterable[dict]:
    """Функция, возращающее  итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной"""
    for info in info_transfer:
        if info.get("currency") == str(value):
            yield info









