# test_has_liked.py

from utils.getLikingUsers import getLikingUsers

async def hasLiked(username, tweet_Id):
    userList = await getLikingUsers(tweetId=tweet_Id)
    exists = username in userList
    print("Exists:", exists)
    return exists

