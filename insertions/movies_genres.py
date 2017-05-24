import csv
import json
import pandas as pd
import sys, getopt, pprint
from pymongo import MongoClient
#CSV to JSON Conversion
csvfile = open('C://tmp//movies_genres.csv', 'r')
reader = csv.DictReader(csvfile)
client = MongoClient('localhost', 27017)
db = client.IMDB
db.movies_genres.drop()
header = [ "idmovies_genres", "idmovies", "idgenres", "idseries"]

for each in reader:
    row = {}
    for field in header:
        row[field] = each[field]

    db.movies_genres.insert(row)

