from pymongo import MongoClient
from pymongo.errors import PyMongoError
from bson.objectid import ObjectId 


class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB"""

    def __init__(self, user, password):
        # Connection variables
        USER = user
        PASS = password
        HOST = 'localhost'
        PORT = 27017
        DB = 'aac'
        COL = 'animals'

        # Initialize connection
        self.client = MongoClient(
            'mongodb://%s:%s@%s:%d/?authSource=admin' % (USER, PASS, HOST, PORT)
        )
        self.database = self.client[DB]
        self.collection = self.database[COL]

    # Create method to implement the C in CRUD
    def create(self, data):
        if data is not None:
            try:
                self.collection.insert_one(data)
                return True
            except PyMongoError:
                return False
        else:
            return False

    # Read method to implement the R in CRUD
    def read(self, query):
        if query is not None:
            try:
                data = self.collection.find(query, {"_id": False})
                return list(data)
            except PyMongoError:
                return []
            
        # Update method
    def update(self, query, new_values):
        if query is not None and new_values is not None:
            try:
                result = self.collection.update_many(query, {"$set": new_values})
                return result.modified_count
            except PyMongoError:
                return 0
        else:
            return 0

    # Delete method
    def delete(self, query):
        if query is not None:
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count
            except PyMongoError:
                return 0
        else:
            return 0