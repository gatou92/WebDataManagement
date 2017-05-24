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
