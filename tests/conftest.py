import pytest


@pytest.fixture
def test_same_date():
    return (
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
    )


import pytest


@pytest.fixture
def ops_mixed_states_diff_dates():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2019-01-03T10:00:00.000000"},
        {"id": 2, "state": "CANCELED", "date": "2018-12-30T12:00:00.000000"},
        {"id": 3, "state": "EXECUTED", "date": "2020-05-01T09:30:00.000000"},
        {"id": 4, "state": "CANCELED", "date": "2019-01-01T00:00:00.000000"},
    ]


@pytest.fixture
def ops_all_executed_diff_dates():
    return [
        {"id": 10, "state": "EXECUTED", "date": "2021-01-01T00:00:00.000000"},
        {"id": 11, "state": "EXECUTED", "date": "2020-01-01T00:00:00.000000"},
        {"id": 12, "state": "EXECUTED", "date": "2019-01-01T00:00:00.000000"},
    ]


@pytest.fixture
def ops_all_canceled_diff_dates():
    return [
        {"id": 20, "state": "CANCELED", "date": "2021-06-01T00:00:00.000000"},
        {"id": 21, "state": "CANCELED", "date": "2021-05-01T00:00:00.000000"},
    ]


@pytest.fixture
def ops_same_date_mixed_states():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.fixture
def ops_unsorted_dates():
    return [
        {"id": 31, "state": "EXECUTED", "date": "2019-04-01T00:00:00.000000"},
        {"id": 32, "state": "EXECUTED", "date": "2019-04-03T00:00:00.000000"},
        {"id": 33, "state": "CANCELED", "date": "2019-04-02T00:00:00.000000"},
    ]


@pytest.fixture
def ops_empty():
    return []


@pytest.fixture
def ops_missing_date_key():
    return [
        {"id": 40, "state": "EXECUTED", "date": "2019-01-01T00:00:00.000000"},
        {"id": 41, "state": "CANCELED"},  # нет date
    ]


@pytest.fixture
def ops_date_is_none():
    return [
        {"id": 50, "state": "EXECUTED", "date": None},
    ]


@pytest.fixture
def ops_date_not_str():
    return [
        {"id": 51, "state": "EXECUTED", "date": 20190703},
    ]


@pytest.fixture
def ops_missing_state_key():
    return [
        {"id": 60, "state": "EXECUTED", "date": "2019-01-01T00:00:00.000000"},
        {"id": 61, "date": "2019-01-02T00:00:00.000000"},  # нет state
    ]


@pytest.fixture
def ops_unknown_state():
    return [
        {"id": 70, "state": "PENDING", "date": "2019-01-01T00:00:00.000000"},
        {"id": 71, "state": "EXECUTED", "date": "2019-01-02T00:00:00.000000"},
    ]

@pytest.fixture
def transactions():
    return [
        {"id": 1, "currency": "USD", "description": "Coffee"},
        {"id": 2, "currency": "EUR", "description": "Book"},
        {"id": 3, "currency": "USD", "description": "Taxi"},
        {"id": 4, "currency": "RUB"},
        {"id": 5, "description": "No currency key"},
    ]