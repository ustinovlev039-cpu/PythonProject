def filter_by_state(diction: list[dict], state="EXECUTED") -> list[dict]:
    """Функция возращающая словарь с соответсвующим ключом state"""
    new_diction = []
    for dict_item in diction:
        if dict_item.get("state") == state:
            new_diction.append(dict_item)

    return new_diction


def sort_by_date(date: list[dict], reverse=True) -> list:
    """Функция сортирующая по датам с возрастающей или по убыванию"""
    result = sorted(date, key=lambda x: x["date"], reverse=True)
    return result


# Добить, чтобы линтеры не выдавали ошибку + сделать слияние веток + добить README