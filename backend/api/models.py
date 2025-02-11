# from django.db import models
from dataclasses import dataclass, field
from typing import List, Dict
from bson import ObjectID
# Create your models here.
@dataclass
class Product:
    """Class for products document"""
    
    # Class attributes start here
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
    reviews: ObjectID = field(default_factory=ObjectID)
    
    