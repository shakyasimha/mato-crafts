from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status 

from .queryset import QuerySet 
from .models import (
    
)

# Create your views here.
@api_view(['GET', 'POST'])
def test_api(request):
    if request.method == 'GET':
        return Response('OK', status=status.HTTP_200_OK)
    
