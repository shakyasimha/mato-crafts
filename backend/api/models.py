# from django.db import models
from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.

# Test models 
class Local(models.Model):
    _DATABASE = 'default'
    
    name = models.CharField(max_length=50)
    data = models.JSONField()
    
class Remote(models.Model):
    _DATABASE = 'remote'
    
    name = models.CharField(max_length=20)
    data = models.JSONField() 

## Tables for application begins here
class Customer(models.Model):
    name = models.CharField(max_length=255, null=False)
    phone = models.CharField(max_length=16, null=False)
    address = models.CharField(max_length=255)
class Employee(models.Model):
    name = models.CharField(max_length=255, null=False)
    address = models.CharField(max_length=255, null=False)
    role = models.CharField(
        max_length=1, 
        choices=[
            ('A', 'Admin'),
            ('M', 'Manager'),
            ('S', 'Salesperson')
        ]
    )
class Product(models.Model):
    name = models.CharField(max_length=255, null=False)
    price = models.FloatField()
    discount = models.IntegerField() 
    stock_remaining = models.IntegerField()
    size = models.CharField(
        max_length=1,
        choices=[
            ('S', 'Small'),
            ('M', 'Medium'),
            ('L', 'Large')
        ]
    )
    images = ArrayField(models.URLField(max_length=255), blank=False, default=list)
    description = models.TextField() 
    materials = ArrayField(models.CharField(max_length=255), blank=True, default=list)
    weight = models.IntegerField()
    dimension = models.CharField(max_length=255)
    type_of = models.CharField(max_length=16, choices=['Pair', 'Single', 'Bundle'])
    # reviews = models.ForeignKey(Review, on_delete=models.SET_NULL, related_name='products')
    categories = models.CharField(max_length=255)
    
class ProductListing(models.Model):
    # product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    quantity = models.IntegerField() 
    listing_price = models.IntegerField() 
    coupon_discount = models.IntegerField()

class Review(models.Model):
    # customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer')
    description = models.TextField() 
    rating = models.IntegerField(max_length=1, choices=[0, 1, 2, 3, 4, 5])
    images = ArrayField(models.URLField(max_length=255), blank=True, default=list)

class Sales(models.Model):
    buyer_name = models.CharField(max_length=255, blank=False)
    price = models.IntegerField()
    verified = models.BooleanField()

class Cart(models.Model):
    paid = models.CharField(max_length=16, choices=['Paid', 'Failed', 'Pending'])


## Junction tables start here
class ProductReviewJunction(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    review_id = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='review')
    
class ProductListingJunction(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    product_listing_id = models.ForeignKey(ProductListing, on_delete=models.CASCADE, related_name='product-listing')


class CartJunction(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    buyer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='buyer')
    product_listing_id = models.ForeignKey(ProductListing, on_delete=models.CASCADE, related_name='products')
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart')

class SalesCartJunction(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    sales_id = models.ForeignKey(Sales, on_delete=models.CASCADE, related_name='sales')
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart')