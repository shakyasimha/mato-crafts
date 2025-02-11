# from django.db import models
from dataclasses import dataclass, field
from typing import List, Dict, Any
from bson import ObjectId
from django.db import models 

# Create your models here.
@dataclass
class Product:
    """Class for products document"""
    _id: ObjectId = field(default_factory=ObjectId)
    name: str = None
    images: List[str] = field(default_factory=list)
    price: int = 0
    stock_remaining: int = 0
    recommender_metadata: Dict[str, Any] = field(default_factory=dict)
    size: List[str] = field(default_factory=list)
    description: str = None
    materials: List[str] = field(default_factory=list)
    weight: int = 0
    dimension: str = None
    product_type: List[str] = field(default_factory=list)
    categories: List[str] = field(default_factory=list)
    _review_id: ObjectId = field(default_factory=ObjectId)
    
    def __post_init__(self):
        """Ensure ObjectIds are valid and convert default values if needed"""
        if not isinstance(self._id, ObjectId):
            self._id = ObjectId(self._id)
        if not isinstance(self._review_id, ObjectId):
            self._review_id = ObjectId(self._review_id)
        
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Product":
        """Create a Product instance from a dictionary (e.g., request.data)"""
        return cls(
            _id=data.get("_id", ObjectId()),
            name=data.get("name"),
            images=data.get("images", []),
            price=data.get("price", 0),
            stock_remaining=data.get("stock_remaining", 0),
            recommender_metadata=data.get("recommender_metadata", {}),
            size=data.get("size", []),
            description=data.get("description"),
            materials=data.get("materials", []),
            weight=data.get("weight", 0),
            dimension=data.get("dimension"),
            product_type=data.get("product_type", []),
            categories=data.get("categories", []),
            _review_id=data.get("_review_id", ObjectId()),
        )    
    
@dataclass 
class Customer: 
    """Class for Customers"""
    _id: ObjectId = field(default_factory=ObjectId)
    phone: str
    name: str = None 
    insta_token: str = None 
    profile_pic: str = None
    address: str = None
    _sales_history_id: List[ObjectId] = field(default_factory=ObjectId)
    
    def __post_init__(self):
        if not isinstance(self._id, ObjectId):
            self._id = ObjectId(self._id) 
        if self.phone is None: 
            raise ValueError("Phone number cannot be null")
        
    
        
@dataclass
class Employee: 
    """Class for employees"""
    _id: ObjectId = field(default_factory=ObjectId)
    name: str = None 
    address: str = None 
    role: List[str] = field(default_factory=list) 
    
    
@dataclass 
class ProductListing:
    """Class for product listing"""
    _product_id: ObjectId = field(default_factory=ObjectId)
    quantity: int = 0 
    listing_price: int = 0 
    coupon_discount: int = 0 
    
@dataclass 
class Sales: 
    """Class for sales/cart"""
    _id: ObjectId = field(default_factory=ObjectId)
    _buyer_id: ObjectId = field(default_factory=ObjectId) 
    price: int = 0 
    verified: bool = False 
    
@dataclass 
class Cart: 
    """Class for cart"""
    _id: ObjectId = field(default_factory=ObjectId)
    _product_listing_id: ObjectId = field(default_factory=ObjectId)
    _buyer_id: ObjectId = field(default_factory=ObjectId)
    paid: List[str] = field(default_factory=list)

@dataclass 
class Review: 
    """Class for review"""
    _id: ObjectId = field(default_factory=ObjectId)
    _customer_id: ObjectId = field(default_factory=ObjectId)
    description: str = None 
    rating: List[int] = [0, 1, 2, 3, 4, 5]
    images: List[str] = field(default_factory=list)