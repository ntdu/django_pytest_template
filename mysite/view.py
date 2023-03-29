import requests
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .my_calendar import abc


@api_view(['GET'])
def get_holidays(request):
    r = requests.get('http://localhost/api/holidays')
    if r.status_code == 200: return Response('serializer.data', status=status.HTTP_201_CREATED)

    return Response('', status=status.HTTP_400_BAD_REQUEST)
