import asyncio
from dotenv import load_dotenv
import os
from pymongo import MongoClient

load_dotenv()

async def getTweeterUsername(discordUsername):
    CONNECTION_STRING = os.getenv("MONGO_URI")

    client = MongoClient(CONNECTION_STRING)

    mydb = client["Cluster0"]  

    myCol = mydb["TUsername"]

    twitterUsername = myCol.find_one({"discord": discordUsername}, {"twitter": 1, "_id": 0})

    if isinstance(twitterUsername, dict) and 'twitter' in twitterUsername:
        return twitterUsername['twitter']  # Return the value of 'twitter' field directly
    else:
        return None

