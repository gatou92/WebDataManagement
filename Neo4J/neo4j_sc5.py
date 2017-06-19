def neo4j_sc5(quer, session):
    diction=[]

    if len(quer) == 2:

        qstat = session.run("MATCH (a:movies) "
                            "-[r:MOVIE_GENRE]->(g:genres) WHERE  a.year = {year}   "
                            "RETURN DISTINCT g.genre, COUNT(r)", {'year': quer[1]})

        for record in qstat:
            print("Genre: %s \n Number of Movies: %s" % (record["g.genre"],record["COUNT(r)"]))
            tempDict = {
                'Genre: ': record["g.genre"],
                'Number of Movies: ': record["COUNT(r)"]
            }
            diction.append(tempDict)

    else:

        qstat = session.run("MATCH (a:movies) "
                            "-[r:MOVIE_GENRE]->(g:genres) WHERE  a.year >= {year} AND  a.year <= {endyear}  "
                            "RETURN DISTINCT g.genre, COUNT(DISTINCT r)", {'year': quer[1], 'endyear': quer[2]})

        for record in qstat:
            print("Genre: %s \n Number of Movies: %s" % (record["g.genre"], record["COUNT(DISTINCT r)"]))
            tempDict = {
                'Genre: ': record["g.genre"],
                'Number of Movies: ': record["COUNT(DISTINCT r)"]
            }
            diction.append(tempDict)

    return diction
