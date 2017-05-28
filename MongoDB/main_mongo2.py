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

        cursor2 = db.movies_genres.aggregate(
            [

                {"$match": {"idmovies": "3"}},
                {
                    "$lookup": {
                        "from": "movies",
                        "localField": "idmovies",
                        "foreignField": "idmovies",
                        "as": "movies1"
                    }
                }
            ])

        cursor3 = db.movies_keywords.aggregate(
            [

                {"$match": {"idmovies": "3"}},
                {
                    "$lookup": {
                        "from": "movies",
                        "localField": "idmovies",
                        "foreignField": "idmovies",
                        "as": "movies1"
                    }
                }
            ])

        cursor4 = db.actors.aggregate(
            [

                {"$match": {"idmovies": "3"}},
                {
                    "$lookup": {
                        "from": "acted_in",
                        "localField": "idactors",
                        "foreignField": "idactors",
                        "as": "actors1"
                    }
                }
            ])
        print 'Cursor'


        for doc in cursor1:
            print(doc)
            #for key in doc.keys():
             #   print(key)

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
            var = doc['idgenres']
            print doc['idgenres']
            cursor_genre = db.genres.find({'idgenres': var})
            for g in cursor_genre:
                print g['genre']
                tempDict = {
                    'Genres': g['genre']
                }
                # append the temporary dictionary to dict
                diction.append(tempDict)

        for doc in cursor3:
#            print(doc)
 #           for key in doc.keys():
  #              print(key)
            var = doc['idkeywords']
   #         print doc['idkeywords']
            cursor_keywords = db.keywords.find({'idkeywords': var})
            for k in cursor_keywords:
    #            print k['keyword']
                tempDict = {
                    'Keywords': k['keyword']
                }
                # append the temporary dictionary to dict
                diction.append(tempDict)

        cursor4 = db.acted_in.aggregate(
            [

                {"$match": {"idmovies": "3"}},
                {
                    "$lookup": {
                        "from": "movies",
                        "localField": "idmovies",
                        "foreignField": "idmovies",
                        "as": "actors1"
                    }
                }
            ])  # .sort( { "billing_position": -1 } )

        print 'Cursor 4'
        for doc in cursor4:
 #           print(doc)
            # for key in doc.keys():
            #   print(key)

            var = doc['idactors']
#            print doc['idactors']
            cursor_actors = db.actors.find({'idactors': var})
            for a in cursor_actors:
     #           print a['fname']
                tempDict = {
                    'First Name': a['fname'],
                    'Last Name': a['fname'],
                    'Gender': a['gender'],
                    'Character': doc['character'],
                    'Billing Position': doc['billing_position']
                }
                # append the temporary dictionary to dict
                diction.append(tempDict)

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
