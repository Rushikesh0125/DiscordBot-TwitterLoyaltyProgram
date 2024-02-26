# verify if user has commented
# verify if user has retweeted
from utils.getCommentedUser import getCommentingUsers

async def hasCommented(username, tweet_Id):
    userList = await getCommentingUsers(tweetId=tweet_Id)
    exists = username in userList
    return exists
