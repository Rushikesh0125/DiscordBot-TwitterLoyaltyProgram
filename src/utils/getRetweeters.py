# returns list of retweeting users
# await gather(api.retweeters(tweet_id, limit=20))

import asyncio
from twscrape import API, gather
from twscrape.logger import set_log_level
from dotenv import load_dotenv
import os

load_dotenv()

async def getRetweetingUsers(tweetId) :
    api = API()

    await api.pool.add_account(os.getenv("USER1"), os.getenv("USER_PASS1"), os.getenv("EMAIL1"), os.getenv("EMAIL_PASS1"))
    await api.pool.add_account(os.getenv("USER2"), os.getenv("USER_PASS2"), os.getenv("EMAIL2"), os.getenv("EMAIL_PASS2"));
    await api.pool.login_all()

    retweeters = await gather(api.retweeters(tweetId, limit=20))
    list = []
    for user in retweeters:
        list.append(user.username)
    return list
