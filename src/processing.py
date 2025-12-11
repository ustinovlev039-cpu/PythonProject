def filter_by_state(list_operation: list[dict], state="EXECUTED") -> list[dict]:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению."""
    new_dictionary = []
    for dict_item in list_operation:
        if dict_item.get("state") == state:
            new_dictionary.append(dict_item)

    return new_dictionary


def sort_by_date(to_do_list: list[dict], reverse=True) -> list:
    """Функция должна возвращать новый список, отсортированный по дате (date)."""
    result = sorted(to_do_list, key=lambda x: x["date"], reverse=True)
    return result



