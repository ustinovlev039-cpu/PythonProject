def filter_by_state(list_operation: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению."""
    allowed = ("EXECUTED", "CANCELED", "PENDING")
    if state not in allowed:
        raise ValueError("Не правильный ввод state")

    new_dictionary = []
    for dict_item in list_operation:
        if dict_item.get("state") == state:
            new_dictionary.append(dict_item)

    return new_dictionary


def sort_by_date(to_do_list: list[dict], reverse=True) -> list[dict]:
    """Функция должна возвращать новый список, отсортированный по дате (date)."""
    for item in to_do_list:
        if "date" not in item:
            raise KeyError("data")
        if not isinstance(item["date"], str):
            raise TypeError("не правильный тип ввода")

    result = sorted(to_do_list, key=lambda x: x["date"], reverse=reverse)
    return result
