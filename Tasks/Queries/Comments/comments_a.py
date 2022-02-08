# Find top 10 users who made the maximum number of comments

from comments import db, collection

result = collection.aggregate([
    {"$group": {"_id": {"user": "$name", "email": "$email"}, "TotalComments": {"$sum": 1}}},
    {"$project": {"user_name": "$_id.user", "user_email": "$_id.email", "TotalComments": 1, "_id": 0}},
    {"$sort": {"TotalComments": -1}},
    {"$limit": 10}
])

for i in result:
    print(i)
