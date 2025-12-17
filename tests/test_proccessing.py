import pytest

from src.processing import filter_by_state
from src.processing import sort_by_date

operation = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

operation_not_match = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
]

operation_date = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

same_date = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
]


@pytest.mark.parametrize(
    "state, dict_result",
    [
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
    ],
)
def test_filter_by_state(state, dict_result):
    assert filter_by_state(operation, state) == dict_result


def test_filter_by_state_not_match():
    assert filter_by_state(operation_not_match, "CANCELED") == []


def test_raises_filter_by_state():
    with pytest.raises(ValueError, match="Не правильный ввод state"):
        filter_by_state(operation, "EXECEIVEV")


@pytest.mark.parametrize(
    "info_sort, result_date",
    [
        (
            True,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            False,
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
    ],
)
def test_sort_by_date(info_sort, result_date):
    assert sort_by_date(operation_date, info_sort) == result_date


def test_sort_by_date_same(test_same_date):
    assert sort_by_date(test_same_date) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
    ]


def test_sort_by_date_not_string():
    string_date = [
        {"id": 1, "state": "EXECUTED", "date": 123456},
        {"id": 2, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]

    with pytest.raises(TypeError):
        sort_by_date(string_date)


def test_sort_by_date_none():
    none_date = [
        {"id": 1, "state": "EXECUTED", "date": None},
        {"id": 2, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]

    with pytest.raises(TypeError):
        sort_by_date(none_date)


def test_sort_by_not_data():
    not_data = [{"id": 1, "state": "EXECUTED"}]

    with pytest.raises(KeyError):
        sort_by_date(not_data)
