from rest_framework.serializers import ModelSerializer 

from .models import (
    Product,
    ProductListing,
    Review,
    Sales, 
    Cart, 
    Customer, 
    Employee,
)

# Serializers go here
class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product 
        fields = ['name', 'price', 'discount', 'stock_remaining', 'size', 'images', 'description', 'materials', 'weight', 'dimension', 'typeof', 'categories']
    
class ProductListingSerializer(ModelSerializer):
    class Meta:
        model = ProductListing
        fields = ['product_id', 'review_id']
        
class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = ['description', 'rating', 'images']

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