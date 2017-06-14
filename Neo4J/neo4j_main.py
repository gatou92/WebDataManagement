from flask_restful import Api, Resource
from flask import request, jsonify, Flask, Blueprint

from neo4j.v1 import GraphDatabase, basic_auth

from neo4j_sc1 import neo4j_sc1
from neo4j_sc2 import neo4j_sc2
from neo4j_sc3 import neo4j_sc3
from neo4j_sc4 import neo4j_sc4
from neo4j_sc5 import neo4j_sc5

class Queries(Resource):
    def get(self):

        driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", "1234"))
        session = driver.session()

        # receive argument from url
        sc = request.args.get('sc_arg')

        # split argument with dash as seperator
        # save results to quer
        quer = sc.split('_')

        # quer[0] shows the service controller
        print 'Service Controller:' + quer[0]

        if quer[0] == 'sc1':
            diction = neo4j_sc1(quer, session)
        if quer[0] == 'sc2':
            diction = neo4j_sc2(quer, session)
        if quer[0] == 'sc3':
            diction = neo4j_sc3(quer, session)
        if quer[0] == 'sc4':
            diction = neo4j_sc4(quer, session)
        if quer[0] == 'sc5':
            diction = neo4j_sc5(quer, session)

        return jsonify(diction)


# initialise constants
api_bp = Blueprint('api', __name__)
api = Api(api_bp)
api.add_resource(Queries, '/user/query/')

app = Flask(__name__)
app.register_blueprint(api_bp)


@app.route('/')
def index():
    return jsonify({'status': 200, 'success': True})


# determine host and port
app.run(host='localhost', port=9090)