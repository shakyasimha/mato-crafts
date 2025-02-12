from django.urls import path 
from .views import (
    test_api,
    product_view, 
)

urlpatterns = [
    path('', test_api, name='index'),
    path('/products', product_view, name='products'),
]