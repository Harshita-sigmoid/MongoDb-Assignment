# Find top 10 movies with most comments

from comments import db, collection

result = collection.aggregate([
    {"$group": {"_id": {"movie_id": "$movie_id"}, "TotalComments": {"$sum": 1}}},
    {"$project": {"movie_id": "$_id.movie_id", "TotalComments": 1, "_id": 0}},
    {"$sort": {"TotalComments": -1}},
    {"$limit": 10}
])

for i in result:
    print(i)
