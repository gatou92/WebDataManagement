import csv
import json
import pandas as pd
import sys, getopt, pprint
from pymongo import MongoClient
#CSV to JSON Conversion
csvfile = open('C://tmp//actors.csv', 'r')
reader = csv.DictReader(csvfile)
client = MongoClient('localhost', 27017)
db = client.IMDB
db.actors.drop()
header = [ "idactors", "lname", "fname", "mname", "gender", "number"]

for each in reader:
    row = {}
    for field in header:
        row[field] = each[field]

    db.actors.insert(row)
