import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()


class MongoDB:

    def __init__(self):
        use_mongo = os.getenv("USE_MONGO", "false").lower() == "true"

        if not use_mongo:
            self.enabled = False
            return

        env = os.getenv("ENVIRONMENT", "local")

        if env == "docker":
            uri = os.getenv("MONGO_URI_DOCKER")
        else:
            uri = os.getenv("MONGO_URI_LOCAL")

        db_name = os.getenv("MONGO_DB", "default_db")

        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db["executions"]
        self.enabled = True

    def insert(self, data: dict):
        if not self.enabled:
            return None

        return self.collection.insert_one(data)