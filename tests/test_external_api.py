from unittest.mock import Mock
from unittest.mock import patch

from src.external_api import conversation
from src.external_api import filter_transactions
from src.utils import info_transactions_json

info_json = info_transactions_json()


@patch("src.external_api.requests.get")
def test_filter_transactions_usd(mock_get_usd):
    fake_response = Mock()
    fake_response.json.return_value = {"result": "661024.933223"}

    mock_get_usd.return_value = fake_response
    result = conversation({"from": "USD", "to": "RUB", "amount": "8221.37"})

    assert result == "661024.933223"
    mock_get_usd.assert_called_once()


def test_filter_transactions():
    assert filter_transactions("41428829", info_json) == {"amount": "8221.37", "from": "USD", "to": "RUB"}
