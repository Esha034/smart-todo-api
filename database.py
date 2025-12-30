from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get MongoDB URI from environment
MONGO_URI = os.getenv("MONGO_URI")

# Create MongoDB client
client = MongoClient(MONGO_URI)

# Select database
db = client["smart_todo_db"]

# Collections
users_collection = db["users"]
tasks_collection = db["tasks"]
