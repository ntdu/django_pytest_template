import unittest
# from.my_calendar import get_holidays
from requests.exceptions import Timeout
from unittest.mock import patch
import pytest
import mock
from .my_calendar import *
import json
# import module


def mocked_abc(a):
    return False 

@patch('mysite.module.module.abc_get')
def test_an(mock_get, client):
    mock_get.return_value = 'daef'
    
    url = ''
    response = client.get(url)
    response_body = response.json()
    print(response_body)
    assert response.status_code == 201
    assert response.json() == 'testdef'
    # assert response.status_code == 201
    
    
# @mock.patch('module.module.abc')
# def test_view(client):
#     mocked_abc.return_value = mock.MagicMock(status_code=200,response=json.dumps({'key':'value'})) 

#     with mock.patch('module.module.get_holidays.requests.get') as mock_get:
#         mock_get.return_value.status_code = 200
#         mock_get.return_value.json.return_value = {'key':'value'}
#         url = ''
#         response = client.get(url)

#     assert response.status_code == 201