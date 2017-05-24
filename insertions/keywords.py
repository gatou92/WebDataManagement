import csv
import json
import pandas as pd
import sys, getopt, pprint
from pymongo import MongoClient
#CSV to JSON Conversion
csvfile = open('C://tmp//keywords.csv', 'r')
reader = csv.DictReader(csvfile)
client = MongoClient('localhost', 27017)
db = client.IMDB
db.keywords.drop()
header = [ "idkeywords", "keyword"]

for each in reader:
    row = {}
    for field in header:
        row[field] = each[field]

    db.keywords.insert(row)
