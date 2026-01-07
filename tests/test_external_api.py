import json
from unittest.mock import patch

from src.external_api import conversation
from src.external_api import filter_transactions
from src.utils import info_transactions_json

transactions_usd = {
    "id": 939719570,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
    "description": "Перевод организации",
    "from": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702",
}

transactions_rub = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589",
}


@patch("src.external_api.requests.get")
def test_conversation(mock_get):
    mock_get.return_value.json.return_value = {"result": "123.45"}
    assert conversation({"from": "USD", "to": "RUB", "amount": "1"}) == 123.45
    mock_get.assert_called_once()


@patch("src.external_api.conversation")
def test_filter_transactions_usd(mock_conversation_usd):
    mock_conversation_usd.return_value = 795759.926329
    assert filter_transactions(transactions_usd) == 795759.926329
    mock_conversation_usd.assert_called_once()


@patch("src.external_api.conversation")
def test_filter_transaction_rub(mock_conversation_rub):
    assert filter_transactions(transactions_rub) == 31957.58
    mock_conversation_rub.assert_not_called()


@patch("builtins.open")
def test_info_transactions_open(mock_file_not_found):
    mock_file_not_found.side_effect = FileNotFoundError()
    assert info_transactions_json("no_such_file.json") == []
    mock_file_not_found.assert_called_once()


@patch("builtins.open")
@patch("src.utils.json.load")
def test_info_transactions_json_load(mock_load, _):
    mock_load.side_effect = json.JSONDecodeError("x", "y", 0)
    assert info_transactions_json("no_decode") == []
    mock_load.assert_called_once()
