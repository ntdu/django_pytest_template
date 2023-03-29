from unittest.mock import patch
from app.fetch_www import parse

@patch('app.fetch_www.fetch_net')
def test_an(mock_get):
    mock_get.return_value = 'def'
    assert parse() == 'def123'
    