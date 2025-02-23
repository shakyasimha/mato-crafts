from django.urls import path 
from .views import (
    ProductView,
    ReviewFetchView,
    ProductListingView
)

urlpatterns = [
    path('products/', ProductView.as_view(), name='products'),
    path('products/:id', ProductView.as_view(), name='product'),
    path('products/review/:id', ReviewFetchView.as_view(), name='review'),
    path('products/listing', ProductListingView.as_view(), name='product-listing')
]