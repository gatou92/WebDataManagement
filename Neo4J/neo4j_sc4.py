def neo4j_sc4(quer, session):
    diction=[]

    if len(quer)==3:

        qstat = session.run("MATCH (a:movies) "
                            "-[r:MOVIE_GENRE]->(g:genres) WHERE g.genre = {genre} AND a.year = {year} "
                            "RETURN a.title , a.year ORDER BY a.year, a.title", {'genre': quer[1] ,'year': quer[2]})

        for record in qstat:
            print("Title of Movie : %s \nYear: %s\n" % (record["a.title"], record["a.year"]))
            tempDict = {
                'Title of Movie: ': record["a.title"],
                'Year: ': record["a.year"]
            }
            diction.append(tempDict)

    else:
        qstat = session.run("MATCH (a:movies) "
                            "-[r:MOVIE_GENRE]->(g:genres) WHERE g.genre = {genre} AND a.year >= {year} AND a.year <= {endyear} "
                            "RETURN a.title , a.year ORDER BY a.year, a.title", {'genre': quer[1], 'year': quer[2], 'endyear': quer[3]})

        for record in qstat:
            print("Title of Movie : %s \nYear: %s\n" % (record["a.title"], record["a.year"]))
            tempDict = {
                'Title of Movie: ': record["a.title"],
                'Year: ': record["a.year"]
            }
            diction.append(tempDict)



    return diction
