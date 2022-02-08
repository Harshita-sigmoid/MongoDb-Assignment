# Find N actors who starred in the maximum number of movies in a given year

from movies import db, collection

try:
    def func(n, year):
        result = collection.aggregate([
            {"$match": {"year": year}},
            {"$unwind": "$cast"},
            {"$group": {"_id": {"actors": "$cast"}, "totalMoviesIn1999": {"$sum": 1}}},
            {"$project": {"actor": "$_id.actors", "totalMoviesIn1999": 1, "_id": 0}},
            {"$sort": {"totalMoviesIn1999": -1}},
            {"$limit": n}
        ])
        return result

except:
    print("error")


limit = int(input("Enter the limit: "))
year = int(input("Enter your year: "))
for i in func(limit, year):
    print(i)
