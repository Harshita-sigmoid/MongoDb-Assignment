from pymongo import MongoClient
import json
from bson import ObjectId

try:
    client = MongoClient('localhost', 27017)
except:
    print("Error in Connect")

db = client['db_users']
collection = db['col_user']


# ======================================================================================================================

# to insert all documents in collection


item_list = []

with open('users.json') as f:
    for json_obj in f:
        if json_obj:
            my_dict = json.loads(json_obj)
            my_dict["_id"] = ObjectId(my_dict["_id"]["$oid"])
            item_list.append(my_dict)

collection.insert_many(item_list)

# =================================================================================================================

# for printing all the entries

result = collection.find({})
count = 0

for i in result:
    print(i)
    count += 1
print(count)

# =================================================================================================================

# to insert one data.

def insert_users(id, name, email, password):
    try:
        data = {
            "_id": id,
            "name": name,
            "email": email,
            "password": password,
        }
        collection.insert_one(data)
        print("Insert Successful")
    except KeyError:
        print("Exception occurred while creating the data: Key not present")
    except Exception:
        print("Error occurred")


insert_users(ObjectId("59b99db4cfa9a34dcd7895b6"), "Robert Stark", "robert_stack@gameofthron.es", "$2b$12$UREFwsRUoyF0CRqGNK0LzO0HM/jLhgUCNNIJ9RJAqMUQ74crlJ1Vu")

# =========================================================================================================================

# result = collection.find({"name": "Robert Stark"})
# for i in result:
#     print(i)