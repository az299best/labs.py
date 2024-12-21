from pymongo import MongoClient


class MongoDBConnectionManager:

    def init(self, uri, db_name):
        self.uri = uri
        self.db_name = db_name
        self.client = None
        self.db = None

    def enter(self):
        self.client = MongoClient(self.uri)
        self.db = self.client(self.db_name)
        return self.db

    def exit(self, exc_type, exc_val, exc_tb):
        if self.client:
            self.client.close()


uri = "mongodb://"
db_name = "my_db"

with MongoDBConnectionManager(uri, db_name) as db:
    user_collection = db.user
    user_collection.insert_one({"name": "Viktor", "age": 25})

    result = user_collection.find_one({"age": 25})
    print("Найдены записи: ", result)