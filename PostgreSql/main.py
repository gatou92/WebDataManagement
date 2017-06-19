from flask_restful import Api, Resource
from flask import request, jsonify, Flask, Blueprint
import psycopg2
from Service_Controller1 import service_controller1
from Service_Controller2 import service_controller2
from Service_Controller3 import service_controller3
from Service_Controller4 import service_controller4
from Service_Controller5 import service_controller5

class Queries(Resource):

    def get(self):

        #receive argument from url
        sc = request.args.get('sc_arg')
        print sc
        quer = sc.split('_')
        print 'Service Controller:'+quer[0]
        print 'Argument' + quer[1]

        #connect to database
        try:
            conn = psycopg2.connect("dbname='IMDB' user='postgres' host='localhost' password='476133'")
        except:
            print "Unable to connect to the database"

        #create cursor for the database
        cur = conn.cursor()

        if quer[0]=='sc1':

            diction = service_controller1(quer, cur)


        if quer[0]=='sc2':
            diction = service_controller2(quer, cur)

        if quer[0]== 'sc3':
            diction = service_controller3(quer, cur)
        if quer[0] == 'sc4':
            diction = service_controller4(quer, cur)

        if quer[0]== 'sc5':
            diction = service_controller5(quer, cur)

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
