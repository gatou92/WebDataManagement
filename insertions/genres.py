import csv
import json
import pandas as pd
import sys, getopt, pprint
from pymongo import MongoClient
#CSV to JSON Conversion
csvfile = open('C://tmp//genres.csv', 'r')
reader = csv.DictReader(csvfile)
client = MongoClient('localhost', 27017)
db = client.IMDB
db.genres.drop()
header = ["idgenres", "genre"]

for each in reader:
    row = {}
    for field in header:
        row[field] = each[field]

    db.genres.insert(row)
