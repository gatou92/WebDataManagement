from flask_restful import Api, Resource
from flask import request, jsonify, Flask, Blueprint
import psycopg2

#function for SC1
#input: query from user Movie ID |||
def service_controller1(quer, cur):
    if quer[1].isdigit():
        # Movie ID is given

        # Queries for SC1 when Movie ID is given
        qmovies = """   SELECT   m.idmovies , m.title , m.year
                                      from movies m
                                      WHERE m.idmovies= %s
                                      AND TYPE=3 """

        qseries = """   SELECT DISTINCT  s.name, s.season, s.number
                                      FROM series s JOIN movies m ON m.idmovies = s.idmovies
                                      WHERE m.idmovies = %s
                                      """
        qgenres = """   SELECT DISTINCT  g.genre
                                      FROM genres g
                                      JOIN movies_genres mg
                                      ON g.idgenres = mg.idgenres
                                      JOIN movies m
                                      ON m.idmovies = mg.idmovies
                                      WHERE m.idmovies = %s
                                     """
        qkeywords = """ SELECT DISTINCT  k.keyword
                                      FROM keywords k
                                      JOIN movies_keywords mk
                                      ON k.idkeywords = mk.idkeywords
                                      JOIN movies m
                                      ON m.idmovies = mk.idmovies
                                      WHERE m.idmovies = %s """

        qactors = """   SELECT DISTINCT  a.fname ,  a.lname , a.gender , ai.character , ai.billing_position  AS Actor
                                      FROM actors a
                                      JOIN acted_in ai
                                      ON a.idactors = ai.idactors
                                      JOIN movies m
                                      ON m.idmovies = ai.idmovies
                                      WHERE m.idmovies = %s
                                      ORDER BY ai.billing_position    """

        # execute movies query
        cur.execute(qmovies, [quer[1]])

        # fetch results
        rows = cur.fetchall()

        # dictionary with results to jsonify
        diction = []

        diction.append("Movie Info")

        # for each row in results
        for row in rows:
            if row is not None:
                # add elements of row to the temporary dictionary
                tempDict = {
                    'ID': row[0],
                    'Title': row[1],
                    'Year': row[2],

                }
                # append the temporary dictionary to dict
                diction.append(tempDict)

        # execute series query
        diction.append("Series Info")
        cur.execute(qseries, [quer[1]])

        rows = cur.fetchall()

        for row in rows:
            if row is not None:
                someDict = {
                    'Series Name': row[0]
                }
                diction.append(someDict)

        # execute genres query
        cur.execute(qgenres, [quer[1]])
        diction.append("Genre Labels")
        rows = cur.fetchall()

        for row in rows:
            print "   ", row[0]
            if row is not None:
                someDict = {
                    'Genre': row[0]

                }
                diction.append(someDict)

        # execute keywords query
        diction.append("Keywords Info")
        cur.execute(qkeywords, [quer[1]])

        rows = cur.fetchall()

        for row in rows:
            if row is not None:
                someDict = {
                    'Keyword': row[0]
                }
                diction.append(someDict)

        # execute actors query
        diction.append("Actors Info")
        cur.execute(qactors, [quer[1]])

        rows = cur.fetchall()

        for row in rows:
            print "   ", row
            if row is not None:
                someDict = {
                    'First Name': row[0],
                    'Last Name': row[1],
                    'Gender': row[2],
                    'Character': row[3],
                    'Billing Position': row[4]
                }
                diction.append(someDict)
    else:
        tit = '%' + quer[1] + '%'
        qmovies = """   SELECT   m.idmovies , m.title , m.year
                                                  from movies m
                                                  WHERE m.title LIKE %s
                                                  AND TYPE=3 """

        qseries = """   SELECT DISTINCT  s.name, s.season, s.number
                                                  FROM series s JOIN movies m ON m.idmovies = s.idmovies
                                                  WHERE m.title LIKE %s
                                                  """
        qgenres = """   SELECT DISTINCT  g.genre
                                                  FROM genres g
                                                  JOIN movies_genres mg
                                                  ON g.idgenres = mg.idgenres
                                                  JOIN movies m
                                                  ON m.idmovies = mg.idmovies
                                                  WHERE m.title LIKE %s
                                                 """
        qkeywords = """ SELECT DISTINCT  k.keyword
                                                  FROM keywords k
                                                  JOIN movies_keywords mk
                                                  ON k.idkeywords = mk.idkeywords
                                                  JOIN movies m
                                                  ON m.idmovies = mk.idmovies
                                                  WHERE m.title LIKE %s """

        qactors = """   SELECT DISTINCT  a.fname ,  a.lname , a.gender , ai.character , ai.billing_position  AS Actor
                                                  FROM actors a
                                                  JOIN acted_in ai
                                                  ON a.idactors = ai.idactors
                                                  JOIN movies m
                                                  ON m.idmovies = ai.idmovies
                                                  WHERE m.title LIKE %s
                                                  ORDER BY ai.billing_position    """

        # execute movies query
        cur.execute(qmovies, [tit])

        # fetch results
        rows = cur.fetchall()

        # dictionary with results to jsonify
        diction = []

        diction.append("Movie Info")

        # for each row in results
        for row in rows:
            if row is not None:
                # add elements of row to the temporary dictionary
                tempDict = {
                    'ID': row[0],
                    'Title': row[1],
                    'Year': row[2],

                }
                # append the temporary dictionary to dict
                diction.append(tempDict)

        # execute series query
        diction.append("Series Info")
        cur.execute(qseries, [tit])

        rows = cur.fetchall()

        for row in rows:
            if row is not None:
                someDict = {
                    'Series Name': row[0]
                }
                diction.append(someDict)

        # execute genres query
        cur.execute(qgenres, [tit])
        diction.append("Genre Labels")
        rows = cur.fetchall()

        for row in rows:
            if row is not None:
                someDict = {
                    'Genre': row[0]

                }
                diction.append(someDict)

        # execute keywords query
        diction.append("Keywords Info")
        cur.execute(qkeywords, [tit])

        rows = cur.fetchall()

        for row in rows:
            if row is not None:
                someDict = {
                    'Keyword': row[0]
                }
                diction.append(someDict)

        # execute actors query
        diction.append("Actors Info")
        cur.execute(qactors, [tit])

        rows = cur.fetchall()

        for row in rows:
            print "   ", row
            if row is not None:
                someDict = {
                    'First Name': row[0],
                    'Last Name': row[1],
                    'Gender': row[2],
                    'Character': row[3],
                    'Billing Position': row[4]
                }
                diction.append(someDict)
    return diction

def service_controller2(quer, cur):
    # queries for actor and movie acted in info when Actor ID is given
    qactorid = """      SELECT a.fname, a.lname,COALESCE(a.gender, 0)
                                   FROM actors a
                                   WHERE a.idactors= %s """

    qactmoviesid = """  SELECT DISTINCT  m.title, m.year
                                   FROM movies m
                                   JOIN acted_in ai
                                   ON m.idmovies = ai.idmovies
                                   JOIN actors a
                                   ON a.idactors = ai.idactors
                                   WHERE a.idactors = %s
                                   ORDER BY m.year """

    # queries for actor and movie acted in info when Actor first or last name is given
    qactorname = """        SELECT a.fname, a.lname, COALESCE(a.gender, 0)
                                       from actors a
                                       WHERE a.fname= %s OR a.lname=%s  """

    qactmoviesname = """    SELECT DISTINCT  m.title, m.year
                                       FROM movies m
                                       JOIN acted_in ai
                                       ON m.idmovies = ai.idmovies
                                       JOIN actors a
                                       ON a.idactors = ai.idactors
                                       WHERE a.fname = %s or a.lname = %s
                                       ORDER BY m.year """

    if quer[1].isdigit():
        # Actor ID is given

        cur.execute(qactorid, [quer[1]])
        rows = cur.fetchall()
        diction = []

        diction.append("Actor Info")
        for row in rows:
            if row is not None:
                someDict = {
                    'First Name': row[0],
                    'Last Name': row[1],
                    'Gender': row[2],
                }
                diction.append(someDict)

            cur.execute(qactmoviesid, [quer[1]])
            rows = cur.fetchall()

            diction.append("Movies Acted Info")
            for row in rows:
                if row is not None:
                    someDict = {
                        'Title': row[0],
                        'Year': row[1]
                    }
                    diction.append(someDict)
    else:
        # Actor first or last name is given

        # argument to pass to query execution
        arg = quer[1], quer[1]
        cur.execute(qactorname, arg)

        # fetch results in rows
        rows = cur.fetchall()
        diction = []

        diction.append("Actor Info")
        for row in rows:
            print "   ", row[0]
            if row is not None:
                someDict = {
                    'First Name': row[0],
                    'Last Name': row[1],
                    'Gender': row[2]
                }
                diction.append(someDict)

                # execute query for movies acted in
        cur.execute(qactmoviesname, arg)
        rows = cur.fetchall()

        diction.append("Movies Acted Info")
        for row in rows:
            print "   ", row[0]
            if row[0] is not None:
                someDict = {
                    'Title': row[0],
                    'Year': row[1],

                }
            diction.append(someDict)
    return diction

def service_controller3(quer, cur):
    # queries for short actor statistics when Actor ID is given
    if quer[1].isdigit():
        qshortactid = """SELECT a.fname , a.lname ,COUNT(DISTINCT m.title) AS number
                                   FROM actors a
                                   JOIN acted_in ai
                                   ON a.idactors=ai.idactors
                                   JOIN movies m
                                   ON ai.idmovies=m.idmovies
                                   WHERE a.idactors = %s
                                   GROUP BY a.fname, a.lname
                                   """

        cur.execute(qshortactid, quer[1])
        rows = cur.fetchall()
        diction = []

        diction.append("Actor Info")
        for row in rows:
            if row is not None:
                someDict = {
                    'First Name': row[0],
                    'Last Name': row[1],
                    'Number of Movies': row[2]
                }

                diction.append(someDict)
    else:
        # Actor first or last name is given
        qshortactname = """SELECT a.fname , a.lname , COUNT(DISTINCT m.title) AS number
                                                   FROM actors a
                                                   JOIN acted_in ai
                                                   ON a.idactors=ai.idactors
                                                   JOIN movies m
                                                   ON ai.idmovies=m.idmovies
                                                   WHERE a.fname = %s or a.lname = %s
                                                   GROUP BY a.fname, a.lname
                                                   """
        arg = quer[1], quer[1]
        cur.execute(qshortactname, arg)
        rows = cur.fetchall()
        diction = []

        diction.append("Actor Info")
        for row in rows:
            print "   ", row[0]
            if row is not None:
                someDict = {
                    'First Name': row[0],
                    'Last Name': row[1],
                    'Number of Movies': row[2]
                }

                diction.append(someDict)

    return diction

def service_controller4(quer, cur ):
    print len(quer)
    if len(quer) == 4:
        # Then start and end year are given as input
        flag = True
    else:
        # Then only one year is given as input
        flag = False

    # query when start and end years are given
    qmoviesend = """    SELECT DISTINCT m.title, m.year
                        FROM movies m
                        JOIN movies_genres mg
                        ON mg.idmovies = m.idmovies
                        JOIN genres g
                        ON mg.idgenres = g.idgenres
                        WHERE g.genre = %s
                        AND m.year >= %s AND m.year <= %s
                        ORDER BY m.year, m.title    """

    # quey when only one year is given
    qmoviestart = """   SELECT DISTINCT m.title, m.year
                        FROM movies m
                        JOIN movies_genres mg
                        ON mg.idmovies = m.idmovies
                        JOIN genres g
                        ON mg.idgenres = g.idgenres
                        WHERE g.genre = %s
                        AND m.year = %s
                        ORDER BY m.year, m.title    """

    if flag == True:
        # execute the first query

        # argument for the first query | genre, start_year, end_year |
        arg = quer[1], quer[2], quer[3]

        # execute the query
        cur.execute(qmoviesend, arg)
    else:
        # execute the second query

        # argument for the first query | genre, year |
        arg = quer[1], quer[2]
        cur.execute(qmoviestart, arg)

    # fetch rows from the query execution
    rows = cur.fetchall()
    diction = []

    for row in rows:
        print "   ", row[0]
        if row is not None:
            someDict = {
                'Title': row[0],
                'Year': row[1]
            }

            diction.append(someDict)
    return diction

def service_controller5(quer, cur):
    print len(quer)
    print

    # query for statistics
    qstat = """ SELECT g.genre, COUNT(DISTINCT m.idmovies) AS number
                           FROM genres g
                           JOIN movies_genres mg
                           ON mg.idgenres=g.idgenres
                           JOIN movies m
                           ON mg.idmovies = m.idmovies
                           WHERE m.year >= %s  AND m.year <= %s
                           GROUP BY g.idgenres
                           ORDER BY g.genre """

    if len(quer) == 3:
        # argument for the query | start_year, end_year |
        arg = quer[1], quer[2]
        # execute statistics query
        cur.execute(qstat, arg)
    else:
        # argument for the query | start_year |
        arg = quer[1], quer[1]
        # execute statistics query
        cur.execute(qstat, arg)

    rows = cur.fetchall()

    # dictionary for json results
    diction = []

    for row in rows:
        if row is not None:
            someDict = {
                'Genre': row[0],
                'Number of movies': row[1]
            }

            diction.append(someDict)
    return diction
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
            conn = psycopg2.connect("dbname='imdb_movies' user='postgres' host='localhost' password='KostisT10@@@'")
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
