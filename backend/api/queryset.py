from pymongo import MongoClient
from pymongo.errors import PyMongoError
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

## Class definition for mongodb queries
class QuerySet:
    """Queryset definition for running operations on mongodb client""" 
    client = None 
    
    def __init__(self, collection_name=None):
        """Ctor"""
        if not collection_name: 
            raise ValueError("`collection_name` cannot be empty.")
        
        try: 
            if not QuerySet.client:
                QuerySet.client = MongoClient(url)  

            self.db = QuerySet.client[db_name]
            self.collection = self.db[collection_name]
        except PyMongoError as e: 
            print(f"Error connecting to MongoDB: {e}")
            raise 
            
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
    
    def delete_all(self):
        """Delete all entries"""
        result = self.collection.delete_many({})
        return result.deleted_count 
    
    def update_one(self, query, update):
        """Update a single document."""
        result = self.collection.update_one(query, {"$set": update})
        return result.modified_count
    
    
    