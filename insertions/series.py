import csv
import json
import pandas as pd
import sys, getopt, pprint
from pymongo import MongoClient
#CSV to JSON Conversion
csvfile = open('C://tmp//series.csv', 'r')
reader = csv.DictReader(csvfile)
client = MongoClient('localhost', 27017)
db = client.IMDB
db.series.drop()
header = [ "idseries", "idmovies", "name", "season", "number"]

for each in reader:
    row = {}
    for field in header:
        row[field] = each[field]

    db.series.insert(row)

#cursor = db.segment.find({'idmovies_keywords':'158713'})


#for doc in cursor:
 #   print(doc)