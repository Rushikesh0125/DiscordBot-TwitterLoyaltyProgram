from dotenv import load_dotenv
import os
import asyncio
from pymongo import MongoClient
from DB.getDB import getCollection

async def has_claimed(username, tweet_id, interaction):
    
    db = await getCollection()

    if(interaction == 0):
        user = db.find_one({"username": username, "claimedTweets.tweetId":tweet_id, "claimedTweets.like":True})
    elif(interaction == 1):
        user = db.find_one({"username": username, "claimedTweets.tweetId": tweet_id, "claimedTweets.comment": True})
    elif(interaction == 2):
        user = db.find_one({"username": username, "claimedTweets.tweetId": tweet_id, "claimedTweets.retweet": True})
    if user:
        return True
    else:
        return False
    



