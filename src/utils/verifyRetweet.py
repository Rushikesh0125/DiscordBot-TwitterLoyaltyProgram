# verify if user has retweeted
from utils.getRetweeters import getRetweetingUsers

async def hasRetweeted(username, tweet_Id):
    userList = await getRetweetingUsers(tweetId=tweet_Id)
    exists = username in userList
    return exists
