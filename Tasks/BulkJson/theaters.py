from pymongo import MongoClient
import json
from bson import ObjectId

try:
    client = MongoClient('localhost', 27017)
except:
    print("Error in Connect")

db = client['db_theaters']
collection = db['col_the']

# ======================================================================================================================

# to insert all documents in collection

item_list = []
#
with open('theaters.json') as f:
    for json_obj in f:
        if json_obj:
            my_dict = json.loads(json_obj)
            my_dict["_id"] = ObjectId(my_dict["_id"]["$oid"])
            my_dict["location"]["geo"]["coordinates"][0] = float(my_dict["location"]["geo"]["coordinates"][0]["$numberDouble"])
            my_dict["location"]["geo"]["coordinates"][1] = float(my_dict["location"]["geo"]["coordinates"][1]["$numberDouble"])
            item_list.append(my_dict)

collection.insert_many(item_list)
#
# print(db.col_theaters.find({"location.address.street1": "340 W Market"}).pretty())


# ======================================================================================================================

# to insert one data

def insert_theatres(kwargs):  # function to insert data
    try:
        data = {
            "_id": kwargs["_id"],
            "theaterId": {
                "$numberInt": kwargs["theaterId"],
            },
            "location": {
                "address": kwargs["address"],
                "geo": {
                    "type": kwargs["geo_type"],
                    "coordinates": [kwargs["geo_cx"], kwargs["geo_cy"]]
                }
            }
        }
        collection.insert_one(data)
        print("Insert Successful")
    except KeyError:
        print("Exception occurred while creating the data: Key not present")
    except Exception:
        print("Error occurred")


dict_data = {
    "_id": ObjectId("59a47286cfa9a3a73e51e70c"),
    "theaterId": "1002",
    "address": {
        "street1": "340 W Market",
        "city": "Bloomington",
        "state": "MN",
        "zipcode": "55425"
    },
    "geo_type": "Point",
    "geo_cx": "-93.24565",
    "geo_cy": "44.85466",

}

insert_theatres(dict_data)

# ====================================================================================================================
