from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status 

from .models import (
    Product,
    ProductListing,
    Review,
    Sales, 
    Cart, 
    Customer, 
    Employee,
    CartJunction
)

from .serializer import (
    ProductSerializer, 
    ProductListingSerializer, 
    ReviewSerializer, 
    SalesSerializer, 
    CartSerializer,
    CustomerSerializer,
    EmployeeSerializer
)

# Create your views here.
class ProductView(APIView):
    """
    List or append individual products
    """
    def get(self, request, format=None):
       """Get request goes here"""
       return Response({"message": "OK"}, status=status.HTTP_200_OK)