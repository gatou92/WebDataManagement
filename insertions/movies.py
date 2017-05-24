import csv
import json
import pandas as pd
import sys, getopt, pprint
from pymongo import MongoClient
#CSV to JSON Conversion
csvfile = open('C://tmp//movies.csv', 'r')
reader = csv.DictReader(csvfile)
client = MongoClient('localhost', 27017)
db = client.IMDB
db.movies.drop()
header = [ "idmovies", "title", "year", "number", "type", "location", "language"]

for each in reader:
    row = {}
    for field in header:
        row[field] = each[field]

    db.movies.insert(row)
