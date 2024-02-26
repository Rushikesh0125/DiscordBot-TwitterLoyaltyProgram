import asyncio
import pymongo
from DB.getDB import getCollection

async def toggleClaimed(username, tweetId, interaction):
    db = await getCollection()
    if(interaction == 0):
        await update_claimed_like(username=username, tweet_id=tweetId, db=db)
    elif(interaction == 1):
        await update_claimed_cmnt(username=username, tweet_id=tweetId, db=db)
    elif(interaction == 2):
        await update_claimed_RT(username=username, tweet_id=tweetId, db=db)

    
async def update_claimed_like(username, tweet_id, db):
    # Define the filter to find the user
    filter_query = {"username": username}

    # Check if the claimed tweet with the specified tweet_id exists
    existing_tweet_query = {"username": username, "claimedTweets.tweetId": tweet_id}
    existing_tweet = db.find_one(existing_tweet_query)

    # Update the claimed tweet if it exists
    if existing_tweet:
        update_operation = {"$set": {"claimedTweets.$.like": True}}
        db.update_one(existing_tweet_query, update_operation)
    else:
        # If the claimed tweet doesn't exist, add a new one
        new_tweet = {
            "tweetId": tweet_id,
            "like": True,
            "comment": False,
            "retweet": False
        }
        update_operation = {"$addToSet": {"claimedTweets": new_tweet}}
        db.update_one(filter_query, update_operation)


async def update_claimed_cmnt(username, tweet_id, db):
    # Define the filter to find the user
    filter_query = {"username": username}

    # Check if the claimed tweet with the specified tweet_id exists
    existing_tweet_query = {"username": username, "claimedTweets.tweetId": tweet_id}
    existing_tweet = db.find_one(existing_tweet_query)

    # Update the claimed tweet if it exists
    if existing_tweet:
        update_operation = {"$set": {"claimedTweets.$.comment": True}}
        db.update_one(existing_tweet_query, update_operation)
    else:
        # If the claimed tweet doesn't exist, add a new one
        new_tweet = {
            "tweetId": tweet_id,
            "like": False,
            "comment": True,
            "retweet": False
        }
        update_operation = {"$addToSet": {"claimedTweets": new_tweet}}
        db.update_one(filter_query, update_operation)


async def update_claimed_RT(username, tweet_id, db):
    # Define the filter to find the user
    filter_query = {"username": username}

    # Check if the claimed tweet with the specified tweet_id exists
    existing_tweet_query = {"username": username, "claimedTweets.tweetId": tweet_id}
    existing_tweet = db.find_one(existing_tweet_query)  

    # Update the claimed tweet if it exists
    if existing_tweet:
        update_operation = {"$set": {"claimedTweets.$.retweet": True}}
        db.update_one(existing_tweet_query, update_operation)
    else:
        # If the claimed tweet doesn't exist, add a new one
        new_tweet = {
            "tweetId": tweet_id,
            "like": False,
            "comment": False,
            "retweet": True
        }
        update_operation = {"$addToSet": {"claimedTweets": new_tweet}}
        db.update_one(filter_query, update_operation)


