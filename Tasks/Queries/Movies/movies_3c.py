# Find N actors who starred in the maximum number of movies for a given genre

from movies import db, collection


def func(n, genre):
    result = collection.aggregate([
        {"$unwind": "$genres"},
        {"$match": {"genres": genre}},
        {"$unwind": "$cast"},
        {"$group": {"_id": {"actors": "$cast"}, "totalCountOfComedyMovies": {"$sum": 1}}},
        {"$project": {"actor": "$_id.actors", "totalCountOfComedyMovies": 1, "_id": 0}},
        {"$sort": {"totalCountOfComedyMovies": -1}},
        {"$limit": n}
    ])
    return result


limit = int(input("Enter the limit: "))
req_genre = input("Enter your genre: ")

for i in func(limit, req_genre):
    print(i)
