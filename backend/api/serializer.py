from rest_framework.serializers import ModelSerializer 

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

# Serializers go here
class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product 
        fields = "__all__"
    
class ProductListingSerializer(ModelSerializer):
    class Meta:
        model = ProductListing
        fields = "__all__"
        
class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

class SalesSerializer(ModelSerializer):
    class Meta:
        model = Sales
        fields = "__all__"
        
class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart 
        fields = "__all__"
        
class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee 
        fields = "__all__"