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
    List or add individual products
    """
    def get(self, request, format=None):
       """Get request goes here"""
        try:
            product_id = request.query_params.get('id')
            
            if product_id:
                product = Product.objects.get(id=product_id)
                serializer = ProductSerializer(product)
            else:
                product = Product.objects.all()
                serializer = ProductSerializer(product, many=True) 
        
            return Response({"products": serializer.data}, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({"error": "Product does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request, format=None):
        """Post request goes here"""
        try: 
            serializer = ProductSerializer(data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response({"product": serializer.data}, status=status.HTTP_201_CREATED)
            else: 
                return Response({"error": serializer.error}, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def put(self, request, pk, format=None):
        """Put request goes here"""
        try: 
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product, data=request.data, partial=True)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else: 
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQEST)
        except Product.DoesNotExist:
            return Response({"error": "Product does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def delete(self, request, pk, format=None):
        """Handle delete request here"""
        try: 
            product = Product.objects.get(pk=pk)
            product.delete()
            
            return Response({"message": "Product deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
            return Response({"error": "Product does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class ReviewFetchView(APIView):
    """
    
    """
    