# Find N directors who created the maximum number of movies in a given year

from movies import db, collection


def fund(n, year):
    result = collection.aggregate([
        {"$match": {"year": year}},
        {"$unwind": "$directors"},
        {"$group": {"_id": {"directors": "$directors"}, "totalMoviesIn1999": {"$sum": 1}}},
        {"$project": {"directors": "$_id.directors", "totalMoviesIn1999": 1, "_id": 0}},
        {"$sort": {"totalMoviesIn1999": -1}},
        {"$limit": n}
    ])

    return result


limit = int(input("Enter your limit: "))
year_data = int(input("Enter your year: "))
for i in fund(limit, year_data):
    print(i)
