from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status 
from bson import ObjectId
from pymongo.errors import PyMongoError 

from .queryset import QuerySet 
from .serializer import MongoSerializer
from .models import (
    Product,
    ProductListing, 
    Customer, 
    Employee, 
    Sales, 
    Cart, 
    Review
)

# Create your views here.
@api_view(['GET', 'POST'])
def test_api(request):
    if request.method == 'GET':
        return Response('OK', status=status.HTTP_200_OK)
    
# Creating a new product entry or retrieving products
@api_view(['GET', 'POST'])
def product_view(request):
    query = QuerySet(collection_name="products") 
    serializer = MongoSerializer()
    
    if request == 'GET':
        _id = request.data.get('_id', None)
        
        if _id:
            if not isinstance(_id, ObjectId):
                _id = ObjectId(_id)
                
            product_list = query.find(_id)
            product = serializer.serialize(product_list)
            
            return Response(product)
        else:
            raise ValidationError("_id is required.")
        
        
    if request == 'POST':
        try:
            product = Product() 
            product.from_dict(request.data)
            product.save()       
        except PyMongoError as e:
            print(str(e))
            return Response({"Error": str(e)})