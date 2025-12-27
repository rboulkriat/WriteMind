import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
MONGO_PORT = int(os.getenv("MONGO_PORT", 27017))
DATABASE_NAME = os.getenv("DATABASE_NAME", "writemind_db")  # <-- bien une string

client = MongoClient(f"mongodb://{MONGO_HOST}:{MONGO_PORT}/")
db = client[DATABASE_NAME]

users_collection = db["users"]
entries_collection = db["entries"]
ai_analyses_collection = db["ai_analyses"]
categories_collection = db["categories"]
