from bson import ObjectId
from datetime import datetime

class MongoSerializer:
    """Custom serializer for MongoDB documents.""" 
    @staticmethod 
    def serializer(document):
        """Convert a MongoDB document to JSON-compatible dict"""
        if not isinstance(document, dict):
            return document     ## returns as-is if not dict
        else:
            serialized_doc = {}
            
            for key, value in document.items():
                if isinstance(value, ObjectId):
                    # Serialize ObjectId to string in json
                    serialized_doc[key] = str(value)
                elif isinstance(value, datetime):
                    # Serialize datetime to ISO format
                    serialized_doc[key] = value.isoformat() 
                elif isinstance(value, list):
                    # Serialize list for json
                    serialized_doc[key] = [MongoSerializer.serializer(item)  for item in value]
                elif isinstance(value, dict):
                    # Serialize dictionary
                    serialized_doc[key] = MongoSerializer.serializer(dict)
                else:
                    # Pass the value 
                    serialized_doc[key] = value
            
            return serialized_doc
        
    @staticmethod 
    def deserializer(json_data):
        """Converting a JSON data to BSON format for MongoDB"""
        if not isinstance(json_data, dict):
            return json_data 
        else:
            deserialized_doc = {}

            for key, value in json_data.items():
                if key == "_id" and isinstance(value, str):
                    try: 
                        deserialized_doc[key] = ObjectId(value) # Convert string to ObjectId
                    except: 
                        deserialized_doc[key] = value 
                elif isinstance(value, str) and MongoSerializer.is_iso_datetime(value):
                    deserialized_doc[key] = datetime.fromisoformat(value)
                elif isinstance(value, list):
                    deserialized_doc[key] = [MongoSerializer.deserializer(item) for item in value]
                elif isinstance(value, dict):
                    deserialized_doc[key] = MongoSerializer.deserializer(value)
                else: 
                    deserialized_doc[key] = value 
                    
            return deserialized_doc
        
    @staticmethod
    def is_iso_datetime(value):
        """Check if string is in iso format"""
        try: 
            datetime.fromisoformat(value)
            return True 
        except ValueError:
            return False
                
        
        