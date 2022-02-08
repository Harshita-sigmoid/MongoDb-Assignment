# Find N movies with the highest IMDB rating in a given year

from movies import db, collection


def func(n, year):
    result = collection.aggregate([
        {"$match": {"year": year}},
        {"$project": {"imdb_rating": "$imdb.rating", "title": 1, "_id": 0}},
        {"$sort": {"imdb_rating": -1}},
        {"$limit": n}
    ])
    return result


limit = int(input("Enter the limit to be listed: "))
year_data = int(input("Enter the year: "))
for i in func(limit, year_data):
    print(i)
