# Find top `N` movies -
# with the highest IMDB rating

from movies import db, collection


def func(n):
    result = collection.aggregate([
        {"$project": {"imdb_rating": "$imdb.rating", "_id": 0, "title": 1}},
        {"$sort": {"imdb_rating": -1}},
        {"$limit": n}
    ])
    return result


limit = int(input("Enter number of data to be listed: "))
for i in func(limit):
    print(i)
