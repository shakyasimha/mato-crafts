from pymongo import MongoClient
from dotenv import load_dotenv
import os 

## Importing dotenv files here
load_dotenv()

## Accessing environment variables
db_name = os.getenv('TEST_DB')
url = os.getenv('MONGODB_LOCAL')

## Test document for testing if the api works; import this and test QuerySet
document = {
  "name": "Earrings",
  "description": "Kaan ma jhundaune kura",
  "qty": 42,
  "price": 100.0,
  "size": "Large",
  "dimensions": "12x34x56 cm",
  "thumbnail": "https://picsum.photos/200/300",
  "images": [
    "https://picsum.photos/200/300",
    "https://picsum.photos/200/300",
    "https://picsum.photos/200/300"
  ]
}


## Initializing mongodb client
client = MongoClient(url)

## Class definition for mongodb queries
class QuerySet:
    """Queryset definition for running operations on mongodb client""" 
    def __init__(self):
        """Ctor"""
        if not hasattr(self.__class__, "client"):
            self.__class__.client = MongoClient(url) 
        self.db = self.client[db_name]
        self.collection = self.db['products']
        
    def insert_one(self, post):
        """Inserting single document into the collection"""
        result = self.collection.insert_one(post)
        return result.inserted_id
    
    def find(self, query=None):
        """Find documents in the collection"""
        if query is None:
            query = {}
        return list(self.collection.find(query))
    
    def find_all(self):
        """Retrieve all documents in the collection"""
        result = self.collection.find({})
        return list(result)
        
    def delete_one(self, query):
        """Delete a single document matching the query"""
        result = self.collection.delete_one(query)
        return result.deleted_count
    
    def update_one(self, query, update):
        """Update a single document."""
        result = self.collection.update_one(query, {"$set": update})
        return result.modified_count
    
    
    