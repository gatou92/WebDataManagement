from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.IMDB

db.movies_with_genres.ensure_index("idmovies")
db.movies_with_genres.ensure_index("genre")
db.movies_with_genres.ensure_index("year")

db.actors_acted_final.ensure_index("idmovies")
db.actors_acted_final.ensure_index("idactors")
db.actors_acted_final.ensure_index("fname")
db.actors_acted_final.ensure_index("lname")
db.series.ensure_index("idmovies")
db.movies_and_keywords.ensure_index("idmovies")
db.movies_with_genres.ensure_index("title")