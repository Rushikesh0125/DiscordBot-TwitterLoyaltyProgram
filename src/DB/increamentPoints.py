import pymongo
from DB.getDB import getCollection

async def increment_points(username, points_to_add):
    # Establish connection to MongoDB
    db = await getCollection()
    user = db.find_one({"username" : username})
    if(user):
        print("found exisiting @increment points")
        prevPoints = user.get("points")
        db.update_one({"username" : username}, { "$set" :{"points" : points_to_add+prevPoints}})
        return
    else:
        print("putting new @increment points")
        user_structure = {
            "username": username,
            "points": points_to_add,
            "claimedTweets": [
                {
                    "tweetId": 0,
                    "like": False,
                    "comment": False,
                    "retweet": False
                }
            ]
        }
        db.insert_one(user_structure)
        return

