import requests
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


def abc_get():
    r = requests.get('http://localhost/api/holidays')
    return 'abc'

@api_view(['GET'])
def get_holidays(request):
    return Response('test' + abc_get(), status=status.HTTP_201_CREATED)
