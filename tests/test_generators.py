import pytest

from src.generators import filter_by_currency
from src.generators import transaction_descriptions
from src.generators import card_number_generator


@pytest.mark.parametrize(
    "value, expected_ids",
    [
        ("USD", [1, 3]),
        ("EUR", [2]),
        ("RUB", [4]),
        ("GBP", []),
        (123, []),
    ],
)
def test_filter_by_currency_filters_correctly(transactions, value, expected_ids):
    result = list(filter_by_currency(transactions, value))
    assert [t["id"] for t in result] == expected_ids


def test_filter_by_currency_absent_currency_returns_empty(transactions):
    assert list(filter_by_currency(transactions, "ZZZ")) == []


@pytest.mark.parametrize("data", [[], [{"id": 1}], [{"id": 1, "currency": "EUR"}]])
def test_filter_by_currency_handles_empty_and_no_matches(data):
    assert list(filter_by_currency(data, "USD")) == []


@pytest.mark.parametrize(
    "data, expected",
    [
        ([], []),
        ([{"description": "A"}], ["A"]),
        ([{"description": "A"}, {"description": "B"}], ["A", "B"]),
        ([{"description": "A"}, {"x": 1}, {"description": "B"}], ["A", "B"]),
        ([{"description": ""}, {"description": "Ok"}], ["Ok"]),  # пустое описание пропускается
    ],
)
def test_transaction_descriptions_returns_descriptions(data, expected):
    assert list(transaction_descriptions(data)) == expected


def test_transaction_descriptions_with_fixture(transactions):
    assert list(transaction_descriptions(transactions)) == ["Coffee", "Book", "Taxi", "No currency key"]



@pytest.mark.parametrize(
    "start, end, expected",
    [
        (1, 1, ["0000 0000 0000 0001"]),
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
        ("9", "10", ["0000 0000 0000 0009", "0000 0000 0000 0010"]),
    ],
)
def test_card_number_generator_range(start, end, expected):
    assert list(card_number_generator(start, end)) == expected


@pytest.mark.parametrize(
    "number, expected",
    [
        (1, "0000 0000 0000 0001"),
        (12, "0000 0000 0000 0012"),
        (1234, "0000 0000 0000 1234"),
        (1234567890123456, "1234 5678 9012 3456"),
    ],
)
def test_card_number_generator_formatting(number, expected):
    assert list(card_number_generator(number, number)) == [expected]


def test_card_number_generator_stops():
    gen = card_number_generator(1, 2)
    assert next(gen) == "0000 0000 0000 0001"
    assert next(gen) == "0000 0000 0000 0002"
    with pytest.raises(StopIteration):
        next(gen)


@pytest.mark.parametrize(
    "start, end",
    [
        (0, 1),
        (1, 0),
        (-1, 5),
        ("-3", "2"),
    ],
)
def test_card_number_generator_non_positive_raises(start, end):
    with pytest.raises(ValueError):
        list(card_number_generator(start, end))


def test_card_number_generator_start_greater_than_end_raises():
    with pytest.raises(ValueError):
        list(card_number_generator(10, 5))
