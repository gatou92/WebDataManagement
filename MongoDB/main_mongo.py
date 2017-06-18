from flask_restful import Api, Resource
from flask import request, jsonify, Flask, Blueprint
import psycopg2
from pymongo import MongoClient
from mongo_sc1 import mongo_sc1
from mongo_sc2 import mongo_sc2
from mongo_sc3 import mongo_sc3
from mongo_sc4 import mongo_sc4
from mongo_sc5 import mongo_sc5
class Queries(Resource):

    def get(self):

        # create MongoClient
        client = MongoClient('localhost', 27017)

        # create database
        db = client.IMDB

        #receive argument from url
        sc = request.args.get('sc_arg')

        #split argument with dash as seperator
        #save results to quer
        quer = sc.split('_')

        #quer[0] shows the service controller
        print 'Service Controller:'+quer[0]

        if quer[0]=='sc1':
            diction = mongo_sc1(quer, db)
        if quer[0] == 'sc2':
            diction = mongo_sc2(quer, db)
        if quer[0] == 'sc3':
            diction = mongo_sc3(quer, db)
        if quer[0] == 'sc4':
            diction = mongo_sc4(quer, db)
        if quer[0] == 'sc5':
            diction = mongo_sc5(quer, db)

        return jsonify(diction)

#initialise constants
api_bp = Blueprint('api', __name__)
api = Api(api_bp)
api.add_resource(Queries, '/user/query/')

app = Flask(__name__)
app.register_blueprint(api_bp)



@app.route('/')
def index():
    return jsonify({'status': 200, 'success': True})

#determine host and port
app.run(host='localhost', port=9090)
