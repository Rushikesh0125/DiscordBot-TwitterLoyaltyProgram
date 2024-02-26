from dotenv import load_dotenv
import os
from pymongo import MongoClient

load_dotenv()

async def getCollection():

    CONNECTION_STRING = os.getenv("MONGO_URI")

    client = MongoClient(CONNECTION_STRING)

    mydb = client["Cluster0"]  

    myCol = mydb["Users"]

    return myCol

