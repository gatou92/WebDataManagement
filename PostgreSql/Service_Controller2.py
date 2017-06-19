def service_controller2(quer, cur):

    print len(quer)

    # queries for actor and movie acted in info when Actor ID is given
    qactorid = """      SELECT a.fname, a.lname,COALESCE(a.gender, 0)
                                   FROM actors a
                                   WHERE a.idactors= %s """

    qactmoviesid = """  SELECT DISTINCT  m.title, m.year, m.idmovies
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

    qactmoviesname = """    SELECT DISTINCT  m.title, m.year, m.idmovies
                                       FROM movies m
                                       JOIN acted_in ai
                                       ON m.idmovies = ai.idmovies
                                       JOIN actors a
                                       ON a.idactors = ai.idactors
                                       WHERE a.fname = %s or a.lname = %s
                                       ORDER BY m.year """

    # queries for actor and movie acted in info when Actor first AND last name are given
    qactornameAND = """        SELECT a.fname, a.lname, COALESCE(a.gender, 0)
                                           from actors a
                                           WHERE a.fname= %s AND a.lname=%s  """

    qactmoviesnameAND = """    SELECT DISTINCT  m.title, m.year, m.idmovies
                                           FROM movies m
                                           JOIN acted_in ai
                                           ON m.idmovies = ai.idmovies
                                           JOIN actors a
                                           ON a.idactors = ai.idactors
                                           WHERE a.fname = %s AND a.lname = %s
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
                        'ID': row[2],
                        'Title': row[0],
                        'Year': row[1]
                    }
                    diction.append(someDict)
    else:
        # Actor first or last name is given

        # argument to pass to query execution
        if len(quer)==3:
            print quer[1]
            if quer[1]=='firstname':
                arg = quer[2], None
            else:
                arg = None, quer[2]
            cur.execute(qactorname, arg)

        else:
            arg = quer[2], quer[3]
            cur.execute(qactornameAND, arg)
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
        if len(quer) == 3:
            print quer[1]
            if quer[1] == 'firstname':
                arg = quer[2], None
            else:
                arg = None, quer[2]
            cur.execute(qactmoviesname, arg)
        else:
            arg = quer[2], quer[3]
            cur.execute(qactmoviesnameAND, arg)
      #  cur.execute(qactmoviesname, arg)
        rows = cur.fetchall()

        diction.append("Movies Acted Info")
        for row in rows:
            print "   ", row[0]
            if row[0] is not None:
                someDict = {
                    'ID': row[2],
                    'Title': row[0],
                    'Year': row[1],

                }
            diction.append(someDict)
    return diction