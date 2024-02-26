import asyncio
from twscrape import API, gather
from twscrape.logger import set_log_level
from dotenv import load_dotenv
import os

load_dotenv()

async def main():
    api = API()  # or API("path-to.db") - default is `accounts.db`

    await api.pool.add_account(os.getenv("USER1"), os.getenv("USER_PASS1"), os.getenv("EMAIL1"), os.getenv("EMAIL_PASS1"));
    # await api.pool.add_account(os.getenv("USER2"), os.getenv("USER_PASS2"), os.getenv("EMAIL2"), os.getenv("EMAIL_PASS2"));
    await api.pool.login_all()

    # or add account with COOKIES (with cookies login not required)
    # cookies = "abc=12; ct0=xyz"  # or '{"abc": "12", "ct0": "xyz"}'
    # await api.pool.add_account("user3", "pass3", "u3@mail.com", "mail_pass3", cookies=cookies)

    # API USAGE

    # tweet info
    tweet_id = "1760927186444288442"
    likes = await gather(api.favoriters(tweet_id, limit=500))  # list[User]
    for user in likes:
        print(user.id, user.username)

    # Note: this method have small pagination from X side, like 5 tweets per query
    # await gather(api.tweet_replies(tweet_id, limit=20))  # list[Tweet]

    # get user by login
    # user_login = "xdevelopers"
    # await api.user_by_login(user_login)  # User

    # user info
    # user_id = 2244994945
    # await api.user_by_id(user_id)  # User
    # await gather(api.following(user_id, limit=20))  # list[User]
    # await gather(api.followers(user_id, limit=20))  # list[User]
    # await gather(api.verified_followers(user_id, limit=20))  # list[User]
    # await gather(api.subscriptions(user_id, limit=20))  # list[User]
    # await gather(api.user_tweets(user_id, limit=20))  # list[Tweet]
    # await gather(api.user_tweets_and_replies(user_id, limit=20))  # list[Tweet]
    # await gather(api.liked_tweets(user_id, limit=20))  # list[Tweet]

    # list info
    # list_id = 123456789
    # await gather(api.list_timeline(list_id))

    # # NOTE 1: gather is a helper function to receive all data as list, FOR can be used as well:
    # async for tweet in api.search("elon musk"):
    #     print(tweet.id, tweet.user.username, tweet.rawContent)  # tweet is `Tweet` object

    # # NOTE 2: all methods have `raw` version (returns `httpx.Response` object):
    # async for rep in api.search_raw("elon musk"):
    #     print(rep.status_code, rep.json())  # rep is `httpx.Response` object

    # # change log level, default info
    # set_log_level("DEBUG")

    # # Tweet & User model can be converted to regular dict or json, e.g.:
    # doc = await api.user_by_id(user_id)  # User
    # doc.dict()  # -> python dict
    # doc.json()  # -> json string

if __name__ == "__main__":
    asyncio.run(main())