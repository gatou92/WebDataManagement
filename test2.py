from flask_restful import Api, Resource
from flask import request, jsonify, Flask, Blueprint
import psycopg2

class SomeClass(Resource):
    def get(self):
        someVar = request.args.get('somevar')
        print someVar
        quer = someVar.split('_')
        print 'query[0]='+quer[0]
        print 'query[1]=' + quer[1]
        print 'query[2]=' + quer[2]
        try:
            conn = psycopg2.connect("dbname='imdb_movies' user='postgres' host='localhost' password='****'")
        except:
            print "I am unable to connect to the database"

        cur = conn.cursor()
        if quer[0]=='movie-info':
            print "Code for movie info query goes here"

            if quer[1]=='id':
                print 'Code for id exact match goes here'
                cur.execute(""" SELECT   m.year ||', ' || m.title || ',' || g.genre AS full_title
                                from movies m join movies_genres mg on m.idmovies=mg.idmovies
                                JOIN genres g on g.idgenres=mg.idgenres
                                WHERE m.idmovies=%s
                                AND TYPE=3
                                GROUP BY m.year, m.title, g.genre
                                ORDER BY m.year, m.title """,[quer[2]])

            if quer[1]=='title':
                print 'Code for title matching goes here'
                print 'title to search = '+quer[2]

                tit = '%'+ quer[2]+'%'
                print 'tit ='+tit
                cur.execute(""" SELECT   m.year ||', ' || m.title || ',' || g.genre    AS full_title
                                FROM movies m JOIN movies_genres mg on m.idmovies=mg.idmovies
                                JOIN genres g on g.idgenres=mg.idgenres
                                WHERE m.title LIKE %s
                                AND type=3
                                GROUP BY m.year, m.title, g.genre
                                ORDER BY m.year, m.title """, [tit])


            rows = cur.fetchall()

            print "\nShow me the databases:\n"
            i=0
            dict = []
            for row in rows:
                print "   ", row[0]
                if row[0] is not None:
                    sp = row[0].split(',')
                    someDict = {
                    'Year': sp[0],
                    'Title': sp[1],
                    'Genre': sp[2]
                    }
                dict.append(someDict)
        # return None, 404
        return jsonify(dict)


api_bp = Blueprint('api', __name__)
api = Api(api_bp)
api.add_resource(SomeClass, '/user/query/')

app = Flask(__name__)
app.register_blueprint(api_bp)



@app.route('/')
def index():
    return jsonify({'status': 200, 'success': True})


app.run(host='localhost', port=9090)
