import asyncio
import pymongo
from DB.getDB import getCollection

async def getLeaders():
    # Establish connection to MongoDB
    db = await getCollection()
    
    pipeline = [
        {
            "$project": {
                "_id": 0,
                "username": 1,
                "points": 1
            }
        },
        {
            "$sort": {"points": -1}  # Sort documents by points in descending order
        },
        {
            "$limit": 5  # Limit the results to the top 5
        }
    ]

    # Execute the aggregation pipeline
    top_5_users = db.aggregate(pipeline)
    list = []
    print("Top 5 Users with the Most Points:")
    for user in top_5_users:
        list.append({"discUsername":user['username'],"points":user['points']})
    return list
    
