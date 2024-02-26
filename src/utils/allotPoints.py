# allot points in DB based on type of interaction
# add to existing points
from utils.verifyComment import hasCommented
from utils.verifyLiked import hasLiked
from utils.verifyRetweet import hasRetweeted
from DB.increamentPoints import increment_points
from DB.toggleClaimed import toggleClaimed
from DB.getTweetUsername import getTweeterUsername

async def allotPointsToInteraction(interaction, tweetId, username, discord) :

    points = 0

    if(interaction == 0):
        print("like interaction points allocation @allot points")
        if(await hasLiked(username, tweetId) == False):
            await print("has not liked tweet @allot points")
            return 0
        points=5
    elif(interaction == 1):
        if(await hasCommented(username, tweetId) == False):
            return 0
        points=10
    elif(interaction == 2):
        if(await hasRetweeted(username, tweetId) == False):
            return 0
        points=15

    await increment_points(username=discord, points_to_add=points)
    await toggleClaimed(username=discord, tweetId=tweetId, interaction=interaction)
    return points
    