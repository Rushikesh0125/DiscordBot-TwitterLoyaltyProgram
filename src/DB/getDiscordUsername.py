import asyncio
from dotenv import load_dotenv
import os
from pymongo import MongoClient

load_dotenv()

async def getDiscordUsername(tweeterUsername):
    CONNECTION_STRING = os.getenv("MONGO_URI")

    client = MongoClient(CONNECTION_STRING)

    mydb = client["Cluster0"]  

    myCol = mydb["TUsername"]

    discordUsername = myCol.find_one({"twitter": tweeterUsername}, {"discord": 1, "_id": 0})

    if isinstance(discordUsername, dict) and 'discord' in discordUsername:
        return discordUsername['discord']  # Return the value of 'twitter' field directly
    else:
        return None

