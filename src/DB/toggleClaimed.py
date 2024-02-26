import asyncio
import pymongo
from DB.getDB import getCollection

async def toggleClaimed(username, tweetId, interaction):
    db = await getCollection()
    if(interaction == 0):
        print("L1")
        await update_claimed_like(username=username, tweet_id=tweetId, db=db)
    elif(interaction == 1):
        print("C1")
        await update_claimed_cmnt(username=username, tweet_id=tweetId, db=db)
    elif(interaction == 2):
        print("R1")
        await update_claimed_RT(username=username, tweet_id=tweetId, db=db)

    
async def update_claimed_like(username, tweet_id, db):
    # Define the filter to find the user
    print("L2")
    filter_query = {"username": username}

    # Check if the claimed tweet with the specified tweet_id exists
    print("L3")
    existing_tweet_query = {"username": username, "claimedTweets.tweetId": tweet_id}
    print("L4")
    existing_tweet = db.find_one(existing_tweet_query)

    # Update the claimed tweet if it exists
    print("L5")
    if existing_tweet:
        print("L6")
        update_operation = {"$set": {"claimedTweets.$.like": True}}
        db.update_one(existing_tweet_query, update_operation)
    else:
        # If the claimed tweet doesn't exist, add a new one
        print("L6")
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
    print("C2")
    filter_query = {"username": username}

    # Check if the claimed tweet with the specified tweet_id exists
    print("C3")
    existing_tweet_query = {"username": username, "claimedTweets.tweetId": tweet_id}
    print("C4")
    existing_tweet = db.find_one(existing_tweet_query)

    # Update the claimed tweet if it exists
    print("C5")
    if existing_tweet:
        print("C6")
        update_operation = {"$set": {"claimedTweets.$.comment": True}}
        print("C7")
        db.update_one(existing_tweet_query, update_operation)
        print("C8")
    else:
        # If the claimed tweet doesn't exist, add a new one
        print("C6")
        new_tweet = {
            "tweetId": tweet_id,
            "like": False,
            "comment": True,
            "retweet": False
        }
        print("C7")
        update_operation = {"$addToSet": {"claimedTweets": new_tweet}}
        print("C8")
        db.update_one(filter_query, update_operation)
        print("C9")


async def update_claimed_RT(username, tweet_id, db):
    # Define the filter to find the user
    print("R2")
    filter_query = {"username": username}

    # Check if the claimed tweet with the specified tweet_id exists
    print("R3")
    existing_tweet_query = {"username": username, "claimedTweets.tweetId": tweet_id}
    print("R4")
    existing_tweet = db.find_one(existing_tweet_query)  

    # Update the claimed tweet if it exists
    print("R5")
    if existing_tweet:
        print("R6")
        update_operation = {"$set": {"claimedTweets.$.retweet": True}}
        db.update_one(existing_tweet_query, update_operation)
    else:
        # If the claimed tweet doesn't exist, add a new one
        print("R6")
        new_tweet = {
            "tweetId": tweet_id,
            "like": False,
            "comment": False,
            "retweet": True
        }
        update_operation = {"$addToSet": {"claimedTweets": new_tweet}}
        db.update_one(filter_query, update_operation)


