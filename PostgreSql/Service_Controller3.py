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

        # Actor first and last name are given
        qshortactnameAND = """SELECT a.fname , a.lname , COUNT(DISTINCT m.title) AS number
                                                           FROM actors a
                                                           JOIN acted_in ai
                                                           ON a.idactors=ai.idactors
                                                           JOIN movies m
                                                           ON ai.idmovies=m.idmovies
                                                           WHERE a.fname = %s AND a.lname = %s
                                                           GROUP BY a.fname, a.lname
                                                           """
        if len(quer) == 3:
            print quer[1]
            if quer[1] == 'firstname':
                arg = quer[2], None
            else:
                arg = None, quer[2]
            cur.execute(qshortactname, arg)
        else:
            arg = quer[2], quer[3]
            cur.execute(qshortactnameAND, arg)

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