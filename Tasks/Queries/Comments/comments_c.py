# Given a year find the total number of comments created each month in that year

from comments import db, collection


def func(year):
    result = collection.aggregate([
        {"$project": {"_id": 0, "date": {"$toDate": {"$convert": {"input": "$date", "to": "long"}}}, "text": 1}},
        {"$project": {"month": {"$month": "$date"}, "year": {"$year": "$date"}, "text": 1}},
        {"$match": {"year": {"$eq": year}}},
        {"$group": {"_id": {"month": "$month"}, "TotalComments": {"$sum": 1}}},
        {"$project": {"month": "$_id.month", "TotalComments": 1, "_id": 0}},
        {"$sort": {"month": 1}}
    ])

    return result


year_data = int(input("Enter the year: "))
for i in func(year_data):
    print(i)
