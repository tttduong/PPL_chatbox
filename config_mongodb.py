# config_mongodb.py
# dùng kết nối mongodb
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from dotenv import load_dotenv
import os 

load_dotenv()
class MongoDBConfig:
    _instance = None
    _client = None
    _db = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MongoDBConfig, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        if self._client is None:
            self.connect()
    
    def connect(self):
        """Kết nối tới MongoDB Atlas"""
        try:
            mongo_uri = os.getenv("MONGO_URI")
            self._client = MongoClient(
                mongo_uri,
                serverSelectionTimeoutMS=5000
            )
            # Test connection
            self._client.admin.command('ping')
            self._db = self._client["ppl_chat"]
            print("✅ MongoDB connected successfully!")
        except ConnectionFailure as e:
            print(f"❌ MongoDB connection failed: {e}")
            raise
    
    def get_db(self):
        """Lấy database instance"""
        if self._db is None:
            self.connect()
        return self._db
    
    def get_collection(self, collection_name):
        """Lấy collection instance"""
        return self.get_db()[collection_name]
    
    def close(self):
        """Đóng kết nối"""
        if self._client:
            self._client.close()
            print("MongoDB connection closed")

# Singleton instance
mongodb = MongoDBConfig()