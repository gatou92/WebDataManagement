import csv
import json
import pandas as pd
import sys, getopt, pprint
from pymongo import MongoClient
#CSV to JSON Conversion
csvfile = open('C://tmp//movies_with_genres.csv', 'r')
reader = csv.DictReader(csvfile)
client = MongoClient('localhost', 27017)
db = client.IMDB

db.movies_with_genres.drop()

header = [ "idmovies_genres", "idmovies", "idgenres", "idseries", "idgenres", "genre",
           "idmovies", "title", "year", "number", "type", "location", "language"]

for each in reader:
    row = {}
    for field in header:
        row[field] = each[field]

    db.movies_with_genres.insert(row)