from dotenv import load_dotenv
import os
from pymongo import MongoClient

load_dotenv()

def create_users_collection():
 
   CONNECTION_STRING = os.getenv("MONGO_URI")
 
   client = MongoClient(CONNECTION_STRING)

   mydb = client["Cluster0"]  

   mycol = mydb["TUsername"]

   user_structure = {
        "discord": "",
        "twitter": ""
    }

   mycol.insert_one(user_structure)

create_users_collection()


