# Find N movies with highest IMDB rating with number of votes > 1000

from movies import db, collection


def func(n):
    result = collection.aggregate([
        {"$match": {"imdb.votes": {"$gt": 1000}}},
        {"$project": {"imdb_rating": "$imdb.rating", "title": 1, "_id": 0}},
        {"$sort": {"imdb_rating": -1}},
        {"$limit": n}
    ])
    return result


n = int(input("Enter the limit: "))
for i in func(n):
    print(i)
