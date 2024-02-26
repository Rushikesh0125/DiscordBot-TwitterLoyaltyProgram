from dotenv import load_dotenv
import os
from pymongo import MongoClient

load_dotenv()

async def getAllTweeterUsername(discordUsername, twitterUsername):
    CONNECTION_STRING = os.getenv("MONGO_URI")

    client = MongoClient(CONNECTION_STRING)

    mydb = client["Cluster0"]  

    myCol = mydb["TUsername"]

    users = myCol.find({})

    list = []

    for user in users:
        list.append(user['twitter'])

    return list
