from pymongo import MongoClient
from dotenv import load_dotenv
import os 

## Importing dotenv files here
load_dotenv()

## Accessing environment variables
username      = os.getenv('DB_USERNAME')
password      = os.getenv('DB_PASSWORD')
atlas_cluster = os.getenv('DB_ATLAS_CLUSTER')
database      = os.getenv('DATABASE_NAME')

## Initializing mongodb client
url = f"mongodb+srv://{username}:{password}@{atlas_cluster}/{database}?retryWrites=true&w=majority"
client      = MongoClient(url)

## Class definition for mongodb queries
class QuerySet:
    """Queryset definition for running operations on mongodb client""" 
    def __init__(self):
        """Ctor"""
        if not hasattr(self.__class__, "client"):
            self.__class__.client = MongoClient(url) 
        self.db = self.client['mato_crafts']
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
    
    
    