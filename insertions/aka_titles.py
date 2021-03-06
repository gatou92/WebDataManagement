import csv
import json
import pandas as pd
import sys, getopt, pprint
from pymongo import MongoClient
#CSV to JSON Conversion
csvfile = open('C://tmp//aka_titles.csv', 'r')
reader = csv.DictReader(csvfile)
client = MongoClient('localhost', 27017)
db = client.IMDB
db.aka_titles.drop()
header = [ "idaka_titles", "idmovies", "title", "location", "year"]

for each in reader:
    row = {}
    for field in header:
        row[field] = each[field]

    db.aka_titles.insert(row)
