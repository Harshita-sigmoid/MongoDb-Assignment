from pymongo import MongoClient
import json
from bson import ObjectId

try:
    client = MongoClient('localhost', 27017)
except:
    print("Error in Connect")

db = client['db_comments']
collection = db['col_comment']

# =================================================================================================================

# to insert all documents in collection

item_list = []

with open('comments.json') as f:
    for json_obj in f:
        if json_obj:
            my_dict = json.loads(json_obj)
            my_dict["_id"] = ObjectId(my_dict["_id"]["$oid"])
            my_dict["date"] = my_dict["date"]["$date"]["$numberLong"]
            my_dict["movie_id"] = my_dict["movie_id"]["$oid"]
            item_list.append(my_dict)

collection.insert_many(item_list)


# =================================================================================================================

# for printing all the entries

# result = collection.find({})
# count = 0
#
# for i in result:
#     print(i)
#     count += 1
# print(count)


# =================================================================================================================

# to insert one data.

def insert_comments(kwargs):  # function to insert data
    try:
        data = {
            "_id": kwargs["_id"],
            "name": kwargs["name"],
            "email": kwargs["email"],
            "movie_id": kwargs["movie_id"],
            "text": kwargs["text"],
            "date": kwargs["date"]
        }
        collection.insert_one(data)
        print("Insert Successful")
    except KeyError:
        print("Exception occurred while creating the data: Key not present")
    except Exception:
        print("Error occurred")


dict_data = {
    "_id": ObjectId("5a9427648b0beebeb69578cc"),
    "name": "Deborah Le",
    "email": "deble@gmail.com",
    "movie_id": "573a13d2f29313caabd91659",
    "text": "Minus libero fuga laudantium. Dolor consequent cumque eos sit. Ex aliquid quas similique accusamu",
    "date": "334443127000"

}
insert_comments(dict_data)

# =================================================================================================================

# result = collection.find({"name": "Deborah Le"})
# for i in result:
#  print(i)
