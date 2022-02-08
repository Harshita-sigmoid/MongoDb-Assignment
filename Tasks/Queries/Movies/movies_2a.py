# Find top `N` directors -
# who created the maximum number of movies

from movies import db, collection


def func(n):
    result = collection.aggregate([
        {"$unwind": "$directors"},
        {"$group": {"_id": {"directors": "$directors"}, "totalMovies": {"$sum": 1}}},
        {"$project": {"directors": "$_id.directors", "totalMovies": 1, "_id": 0}},
        {"$sort": {"totalMovies": -1}},
        {"$limit": n}
    ])
    return result


limit = int(input("Enter your limit: "))
for i in func(limit):
    print(i)
