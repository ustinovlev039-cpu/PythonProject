import pytest

@pytest.fixture
def test_same_date():
    return  (
     {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
     {'id': 615064591, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'}
     )


