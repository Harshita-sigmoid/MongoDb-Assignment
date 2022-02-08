# Find top `N` movies for each genre with the highest IMDB rating

from movies import db, collection


def func(n):
    result = collection.aggregate([
        {"$unwind": "$genres"},
        {"$group": {"_id": {"genres": "$genres"},
                    "filmPlusRating": {"$push": {"title": "$title", "rating": "$imdb.rating"}}}},
        {"$unwind": "$filmPlusRating"},
        {"$sort": {"filmPlusRating.rating": -1}},
        {"$group": {"_id": {"genres": "$_id.genres"}, "filmPlusRating": {"$push": "$filmPlusRating"}}},
        {"$project": {"genre": "$_id.genres", "filmPlusRating": {"$slice": ["$filmPlusRating", n]}, "_id": 0}}
    ])
    return result


for i in func(10):
    print(i)
