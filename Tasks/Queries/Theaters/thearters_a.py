# Top 10 cities with the maximum number of theatres

from theaters import db, collection

try:
    def func():
        result = collection.aggregate([
            {"$group": {"_id": {"city": "$location.address.city"}, "TotalTheaters": {"$sum": 1}}},
            {"$project": {"city": "$_id.city", "TotalTheaters": 1, "_id": 0}},
            {"$sort": {"TotalTheaters": -1}},
            {"$limit": 10}
        ])
        return result


    print("Executed Successfully")
except:
    print("error")


for i in func():
    print(i)
