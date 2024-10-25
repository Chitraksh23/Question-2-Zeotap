from flask import Flask
from pymongo import MongoClient
import os
app = Flask(__name__)
client = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017/"))
db = client.weather_db
from app import main
