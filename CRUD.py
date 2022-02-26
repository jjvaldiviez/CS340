# Create, Read, Update and Destroy script for AnimalShelter database
# Author: Jacob Valdiviez
#
from pymongo import MongoClient


class AnimalShelter:
    # The mongo client
    client = MongoClient()
    # The database of animal shelter
    database = []
    collection = []

    # Initializes the class
    def __init__(self, username, password, port):
        try:
            self.client = MongoClient(f'localhost:{port}')
            self.client.AAC.authenticate(username, password)
            self.database = self.client['AAC']
            self.collection = self.database['animals']

            print('connected!')
        except Exception as e:
            print('can not connect!')
            raise e

    # Inserts to animals given a query
    def create(self, query):
        if query is not None:
            if self.collection.insert_one(query).inserted_id is not None:
                return True
        else:
            raise Exception("Query is empty. Did not inset anything")
        return False

    # Reads one from animals given a query
    def read(self, query):
        if query is not None:
            return self.collection.find(query)
        else:
            raise Exception("Query is empty. Did not read anything")

    # Updates one from animals given a query
    def update(self, query, new_values):
        if query is not None:
            return self.collection.update_many(query, new_values)
        else:
            raise Exception("Query is empty. Did not update anything")

    # Deletes one from animals given a query
    def delete(self, query):
        if query is not None:
            return self.collection.delete_many(query)
        else:
            raise Exception("Query is empty. Did not delete anything")
