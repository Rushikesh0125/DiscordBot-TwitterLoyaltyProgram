from dotenv import load_dotenv
import os
from pymongo import MongoClient

load_dotenv()

def create_users_collection():
 
   CONNECTION_STRING = os.getenv("MONGO_URI")
 
   client = MongoClient(CONNECTION_STRING)

   mydb = client["Cluster0"]  

   mycol = mydb["Users"]

   user_structure = {
        "username": "",
        "points": 0,
        "claimedTweets": [
            {
                "tweetId": 0,
                "like": False,
                "comment": False,
                "retweet": False
            }
        ]
    }

   mycol.insert_one(user_structure)

create_users_collection()


