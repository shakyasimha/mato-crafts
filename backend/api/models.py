# from django.db import models
from dataclasses import dataclass, field
from typing import List, Dict
from bson import ObjectID
# Create your models here.
@dataclass
class Product:
    """Class for products document"""
    _id: ObjectID = field(default_factory=ObjectID)
    name: str = None
    images: List[str] = field(default_factory=list)
    price: int = 0
    stock_remaining: int = 0
    recommender_metadata: Dict[str, any] = field(default_factory=dict)
    size: List[str] = field(default_factory=list)
    description: str = None
    materials: List[str] = field(default_factory=list)
    weight: int = 0
    dimension: str = None
    product_type: List[str] = field(default_factory=list)
    categories: List[str] = field(default_factory=list)
    _review_id: ObjectID = field(default_factory=ObjectID)
    
    
@dataclass 
class Customer: 
    """Class for Customers"""
    _id: ObjectID = field(default_factory=ObjectID)
    phone: str
    name: str = None 
    insta_token: str = None 
    profile_pic: str = None
    address: str = None
    _sales_history_id: List[ObjectID] = field(default_factory=ObjectID)
    
    def __post_init__(self):
        if self.phone is None: 
            raise ValueError("Phone number cannot be null")
        
@dataclass
class Employee: 
    """Class for employees"""
    _id: ObjectID = field(default_factory=ObjectID)
    name: str = None 
    address: str = None 
    role: List[str] = field(default_factory=list) 
    
    
@dataclass 
class ProductListing:
    """Class for product listing"""
    _product_id: ObjectID = field(default_factory=ObjectID)
    quantity: int = 0 
    listing_price: int = 0 
    coupon_discount: int = 0 
    
@dataclass 
class Sales: 
    """Class for sales/cart"""
    _id: ObjectID = field(default_factory=ObjectID)
    _buyer_id: ObjectID = field(default_factory=ObjectID) 
    price: int = 0 
    verified: bool = False 
    
@dataclass 
class Cart: 
    """Class for cart"""
    _id: ObjectID = field(default_factory=ObjectID)
    _product_listing_id: ObjectID = field(default_factory=ObjectID)
    _buyer_id: ObjectID = field(default_factory=ObjectID)
    paid: List[str] = field(default_factory=list)

@dataclass 
class Review: 
    """Class for review"""
    _id: ObjectID = field(default_factory=ObjectID)
    _customer_id: ObjectID = field(default_factory=ObjectID)
    description: str = None 
    rating: List[int] = [0, 1, 2, 3, 4, 5]
    images: List[str] = field(default_factory=list)