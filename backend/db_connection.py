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

## Connection url for mongodb
url = f"mongodb+srv://{username}:{password}@{atlas_cluster}/{database}?retryWrites=true&w=majority"
client = MongoClient(url)

db = client['mato_crafts']