from pymongo import MongoClient
import json
from bson import ObjectId

try:
    client = MongoClient('localhost', 27017)
except:
    print("Error in Connect")

db = client['db_movies']
collection = db['col_movies']

# ======================================================================================================================
#
# # to insert all documents in collection
#
item_list = []

with open('movies.json') as f:
    for json_obj in f:
        if json_obj:
            my_dict = json.loads(json_obj)

            try:
                my_dict["_id"] = ObjectId(my_dict["_id"]["$oid"])
            except:
                pass

            try:
                my_dict["runtime"] = int(my_dict["runtime"]["$numberInt"])
            except:
                pass

            try:
                my_dict["num_mflix_comments"] = int(my_dict["num_mflix_comments"]["$numberInt"])
            except:
                pass

            try:
                my_dict["released"] = my_dict["released"]["$date"]["$numberLong"]
            except:
                pass

            try:
                my_dict["year"] = int(my_dict["year"]["$numberInt"])
            except:
                pass

            try:
                my_dict["imdb"]["rating"] = (my_dict["imdb"]["rating"]["$numberDouble"])
            except:
                pass

            try:
                my_dict["imdb"]["rating"] = (my_dict["imdb"]["rating"]["$numberInt"])
            except:
                pass

            try:
                my_dict["imdb"]["votes"] = int(my_dict["imdb"]["votes"]["$numberInt"])
            except:
                pass

            try:
                my_dict["imdb"]["id"] = int(my_dict["imdb"]["id"]["$numberInt"])
            except:
                pass

            try:
                my_dict["tomatoes"]["viewer"]["rating"] = my_dict["tomatoes"]["viewer"]["rating"]["$numberInt"]
            except:
                pass

            try:
                my_dict["tomatoes"]["viewer"]["rating"] = my_dict["tomatoes"]["viewer"]["rating"]["$numberDouble"]
            except:
                pass

            try:
                my_dict["tomatoes"]["viewer"]["numReviews"] = int(
                    my_dict["tomatoes"]["viewer"]["numReviews"]["$numberInt"])
            except:
                pass

            try:
                my_dict["tomatoes"]["viewer"]["meter"] = int(my_dict["tomatoes"]["viewer"]["meter"]["$numberInt"])
            except:
                pass

            try:
                my_dict["tomatoes"]["lastUpdated"] = my_dict["tomatoes"]["lastUpdated"]["$date"]["$numberLong"]
            except:
                pass

            item_list.append(my_dict)

collection.insert_many(item_list)


#
# =================================================================================================================
#
# # for printing all the entries
#
# result = collection.find({})
# count = 0
#
# for i in result:
#     print(i)
#     count += 1
# print(count)
#
#
# =====================================================================================================================
#
# # to insert one data.
#
def insert_movies(kwargs):  # function to insert data
    movies = db["movies"]
    try:
        data = {
            "_id": kwargs["_id"],
            "plot": kwargs["plot"],
            "genres": kwargs["genres"],
            "runtime": kwargs["runtime"],
            "cast": kwargs["cast"],
            "num_mflix_comments": kwargs["num_mflix_comments"],
            "title": kwargs["title"],
            "fullplot": kwargs["fullplot"],
            "countries": kwargs["countries"],
            "released": kwargs["released_date"],
            "directors": kwargs["directors"],
            "rated": kwargs["rated"],
            "awards": {
                "wins": {
                    "$numberInt": kwargs["awards_wins"]
                },
                "nominations": {
                    "$numberInt": kwargs["awards_nominations"]
                },
                "text": kwargs["awards_text"]
            },
            "lastupdated": kwargs["lastupdated"],
            "year": kwargs["year"],
            "imdb": {
                "rating": kwargs["imdb_rating"],
                "votes": kwargs["imdb_votes"],
                "id": kwargs["imdb_id"],
            },
            "type": kwargs["type"],
            "tomatoes": {
                "viewer": {
                    "rating": kwargs["tomatoes_viewer_rating"],
                    "numReviews": kwargs["tomatoes_viewer_numreviews"],
                    "meter": kwargs["tomatoes_viewer_meter"],
                },
                "lastUpdated": kwargs["tomatoes_lastupdated"],
            }
        }

        movies.insert_one(data)
        print("Insert Successful")
    except KeyError:
        print("Exception occurred while creating the data: Key not present")
    except Exception:
        print("Error occurred")


dict_data = {
    "_id": ObjectId("573a1390f29313caabcd4134"),
    "plot": "Three women hammer on an anvil and pass a bottle of wine around.",
    "genres": [
        "Short",
        "Comedy"
    ],
    "runtime": 13,
    "cast": [
        "Charles Kayser",
        "John Ott"
        "George Barnes",
        "Justus D. Barnes"
    ],
    "num_mflix_comments": 1,
    "title": "Whitesmith Scene",
    "fullplot": "A local camera looks at a small anvil with a whitesmith behind it and one on either side. The smith in the middle draws a heated metal rod from the fire, places it on the anvil, and all three begin a rhythmic hammering. After several blows, the metal goes back in the fire. One smith pulls out a bottle of beer, and they each take a swig. Then, out comes the glowing metal and the hammering resumes.",
    "countries": [
        "USA",
        "India"
    ],
    "released_date": "-2418768000000",
    "directors": [
        "William K.L. Dickson",
        "Edwin S. Porter"
    ],
    "rated": "UNRATED",
    "awards_wins": "1",
    "awards_nominations": "0",
    "awards_text": "1 win.",
    "lastupdated": "2015-08-26 00:03:50.133000000",
    "year": 1893,
    "imdb_rating": "6.2",
    "imdb_votes": 1189,
    "imdb_id": 5,
    "type": "movie",
    "tomatoes_viewer_rating": "3",
    "tomatoes_viewer_numreviews": 184,
    "tomatoes_viewer_meter": 32,
    "tomatoes_lastupdated": "1435516449000"
}

insert_movies(dict_data)

# # ====================================================================================================================
