# from django.db import models
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Any
from bson import ObjectId
from . import queryset 

# Create your models here.
class BaseModel:
    """Base class model to provide shared models"""
    
    @classmethod 
    def from_dict(cls, data: Dict[str, Any]): 
        """Dynamically create an instance of derived class from provided dictionary"""
        field_names = {f.name for f in cls.__dataclass_fields__.values()}
        filtered_data = {k:v for k, v in data.items() if k in field_names}
        
        ## Handling ObjectId fields dynamically 
        for field_name in field_names: 
            field_type = cls.__dataclass_fields__[field_name].type 
            
            if field_type == ObjectId and isinstance(filtered_data.get(field_name), str):
                filtered_data[field_name] = ObjectId(filtered_data[field_name])
                
        return cls(**filtered_data)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert instance to dictionary for MongoDB story"""
        data = asdict(self)
        
        for key, value in data.items():
            if isinstance(value, ObjectId):
                data[key] = str(value)

        return data  
    
    
@dataclass
class Product(BaseModel):
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
    
    def save(self):
        """Save instance to MongoDB"""
        try: 
            db = queryset.QuerySet() 
            result = db.insert_one(self.to_dict())
            return result 
        except Exception as e:
            print(str(e))
            return {"error": str(e)}
    
    
    
@dataclass 
class Customer(BaseModel): 
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
    
    def save(self):
        """Save instance to MongoDB"""
        try: 
            db = queryset.QuerySet() 
            result = db.insert_one(self.to_dict())
            return result 
        except Exception as e:
            print(str(e))
            return {"error": str(e)}
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