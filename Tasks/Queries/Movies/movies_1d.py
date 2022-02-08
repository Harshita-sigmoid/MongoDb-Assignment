# Find N movies with title matching a given pattern sorted by highest tomatoes ratings

from movies import db, collection


def func(n, pattern):
    result = collection.aggregate([
        {"$match": {"title": {"$regex": pattern}}},
        {"$project": {"title": 1, "_id": 0, "tomatoes_rating": "$tomatoes.viewer.rating"}},
        {"$sort": {"tomatoes_rating": -1}},
        {"$limit": n}
    ])

    return result


limit = int(input("Enter your limit: "))
pat = input("Enter your pattern: ")
for i in func(limit, pat):
    print(i)
