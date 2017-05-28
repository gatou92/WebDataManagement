from flask_restful import Api, Resource
from flask import request, jsonify, Flask, Blueprint
import psycopg2

from pymongo import MongoClient

class Queries(Resource):

    def get(self):

        #receive argument from url
        sc = request.args.get('sc_arg')
        print sc
        quer = sc.split('_')
        print 'Service Controller:'+quer[0]
        print 'Argument' + quer[1]

        client = MongoClient('localhost', 27017)
        db = client.IMDB

        cursor = db.movies.find({'idmovies': quer[1]})
        diction = []

        for doc in cursor:
            print(doc)
            print doc['title']
            tempDict = {
                'ID': doc['idmovies'],
                'Title': doc['title'],
                'Year': doc['year']

            }
            # append the temporary dictionary to dict
            diction.append(tempDict)

        cursor1 = db.series.aggregate (
        [
            { "$match": {"idmovies":"3"} },

            {
            "$lookup":{
                    "from": "movies",
                    "localField": "idmovies",
                    "foreignField": "idmovies",
                    "as": "movies_series"
                    }
            }

        ] )

        cursor2 = db.genres.aggregate(
            [
             #   {"$match": {"idmovies": "3"}},

                {
                    "$lookup": {
                        "from": "movies_genres",
                        "localField": "idgenres",
                        "foreignField": "idgenres",
                        "as": "movies1"
                    }
                },
                {
                    "$unwind": "$movies1"
                },

                {
                    "$lookup": {
                        "from": "movies",
                        "localField": "idmovies",
                        "foreignField": "idmovies",
                        "as": "movies2"
                    }
                }


            ])

        print 'Cursor'


        for doc in cursor1:
            print(doc)
            for key in doc.keys():
                print(key)

            tempDict = {
                'Number': doc['number'],
                'Season': doc['season'],
                'Series Name': doc['name']

            }
            # append the temporary dictionary to dict
            diction.append(tempDict)
        print 'Cursor 2'

        for doc in cursor2:
            print(doc)
            for key in doc.keys():
                print(key)

        return jsonify(diction)


api_bp = Blueprint('api', __name__)
api = Api(api_bp)
api.add_resource(Queries, '/user/query/')

app = Flask(__name__)
app.register_blueprint(api_bp)



@app.route('/')
def index():
    return jsonify({'status': 200, 'success': True})


app.run(host='localhost', port=9090)
