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
    ProductListingJunction,
    ProductReviewJunction, 
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
        try: 
            junction_entries = ProductReviewJunction.objects.select_related('product_id', 'review_id').all()
            
            data = []
            
            for entry in junction_entries:
                product = entry.product_id
                review = entry.review_id
                
                ## Serialize the Product and Review 
                product_data = ProductSerializer(product).data
                review_data = ReviewSerializer(review).data 
                
                ## Adding review to product_data 
                combined_data = product_data 
                combined_data["reviews"] = review_data
    
                data.append(combined_data)
                
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {
                    "error": str(e)
                },
                status=status.re
            )