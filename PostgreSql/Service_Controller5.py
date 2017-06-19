#################################################################
#################################################################
###########                                           ###########
###########         PostgreSQL - Fifth Query          ###########
###########                                           ###########
#################################################################
#################################################################

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