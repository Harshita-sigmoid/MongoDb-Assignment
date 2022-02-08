# Find top `N` actors -
# who starred in the maximum number of movies

from movies import db, collection


def func(n):
    result = collection.aggregate([
        {"$unwind": "$cast"},
        {"$group": {"_id": {"actors": "$cast"}, "TotalMovies": {"$sum": 1}}},
        {"$project": {"actors": "$_id.actors", "TotalMovies": 1, "_id": 0}},
        {"$sort": {"TotalMovies": -1}},
        {"$limit": n}
    ])
    return result


limit = int(input("Enter the limit: "))
for i in func(limit):
    print(i)
