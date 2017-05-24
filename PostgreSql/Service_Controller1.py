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