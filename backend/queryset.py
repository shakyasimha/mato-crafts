from pymongo import MongoClient
from dotenv import load_dotenv
import os 

## Importing dotenv files here
load_dotenv()

## Accessing environment variables
db_name = os.getenv('DATABASE_NAME')
url = os.getenv('MONGODB_URL')

## Initializing mongodb client
client = MongoClient(url)

## Test document for testing if the api works; import this and test QuerySet
document = {
  "name": "John Doe",
  "age": 30,
  "email": "john.doe@example.com",
  "address": {
    "street": "123 Main St",
    "city": "New York",
    "state": "NY",
    "zip": "10001"
  },
  "hobbies": ["reading", "traveling", "coding"],
  "is_active": True
}

## Class definition for mongodb queries
class QuerySet:
    """Queryset definition for running operations on mongodb client""" 
    def __init__(self):
        """Ctor"""
        if not hasattr(self.__class__, "client"):
            self.__class__.client = MongoClient(url) 
        self.db = self.client[db_name]
        self.collection = self.db['test']
        
    def insert_one(self, post):
        """Inserting single document into the collection"""
        result = self.collection.insert_one(post)
        return result.inserted_id
    
    def find(self, query=None):
        """Find documents in the collection"""
        if query is None: 
            query = {}
        return list(self.collection.find(query))
    
    def delete_one(self, query):
        """Delete a single document matching the query"""
        result = self.collection.delete_one(query)
        return result.deleted_count
    
    def update_one(self, query, update):
        """Update a single document."""
        result = self.collection.update_one(query, {"$set": update})
        return result.modified_count
    
    
    