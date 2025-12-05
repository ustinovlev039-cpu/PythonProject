def filter_by_state(diction: list[dict], state="EXECUTED") -> list[dict]:
    """Функция возращающая словарь с соответсвующим ключом state"""
    new_diction = []
    for dict_item in diction:
        if dict_item.get("state") == state:
            new_diction.append(dict_item)

    return new_diction


def sort_by_date(date: list[dict], reverse=True) -> list[dict]:
    """Функция сортирующая по датам с возрастающей или по убыванию"""
    result = sorted(date, key=lambda x: x["date"], reverse=True)
    return result


date = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


diction = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

if __name__ == "__main__":
    # print(filter_by_state(diction, state="CANCELED"))
    print(sort_by_date(date))
