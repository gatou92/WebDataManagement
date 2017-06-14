def neo4j_sc2(quer, session):
    diction=[]

    if quer[1].isdigit():

        qactorid = session.run("MATCH (a:actors) WHERE a.idactors = {idactors} "
                               "RETURN a.fname , a.lname , a.gender ", {'idactors':int(quer[1])})

        qactmoviesid = session.run("MATCH (a:actors)"
                           "-[r:ACTED_CHARACTER]->(m:movies) WHERE a.idactors = {idactors}"
                           " RETURN DISTINCT m.idmovies, m.title, m.year ORDER BY m.year DESC", {'idactors':int(quer[1])})

        for record in qactorid:
            print("First Name: %s \nLast Name: %s \nGender: %s\n" % (record["a.fname"], record["a.lname"], record["a.gender"]))
            tempDict={
                'First Name: ': record["a.fname"],
                'Last Name: ': record["a.lname"],
                'Gender: ': record["a.gender"]
            }
            diction.append(tempDict)
        for record in qactmoviesid:
            print("Movie Id: %s \nTitle: %s \nYear: %s\n" % (record["m.idmovies"], record["m.title"], record["m.year"]))
            tempDict={
                'Movie Id: ': record["m.idmovies"],
                'Title: ': record["m.title"],
                'Year: ': record["m.year"]
            }
            diction.append(tempDict)

    else:
        if len(quer) == 3:
            if quer[1] == 'firstname':

                qactorname = session.run("MATCH (a:actors) WHERE a.fname = {fname}"
                                         "RETURN a.fname , a.lname , a.gender ", {'fname':quer[2]})

                qactmoviesname = session.run("MATCH (a:actors)"
                                             "-[r:ACTED_CHARACTER]->(m:movies) WHERE a.fname = {fname} "
                                             " RETURN DISTINCT m.idmovies, m.title, m.year ORDER BY m.year DESC", {'fname':quer[2]})

                for record in qactorname:
                    print("First Name: %s \nLast Name: %s \nGender: %s\n" % (
                    record["a.fname"], record["a.lname"], record["a.gender"]))
                    tempDict = {
                        'First Name: ': record["a.fname"],
                        'Last Name: ': record["a.lname"],
                        'Gender: ': record["a.gender"]
                    }
                    diction.append(tempDict)
                for record in qactmoviesname:
                    print("Movie Id: %s \nTitle: %s \nYear: %s\n" % (
                    record["m.idmovies"], record["m.title"], record["m.year"]))
                    tempDict = {
                        'Movie Id: ': record["m.idmovies"],
                        'Title: ': record["m.title"],
                        'Year: ': record["m.year"]
                    }
                    diction.append(tempDict)

            else:

                qactorname = session.run("MATCH (a:actors) WHERE a.lname = {lname}  "
                                         "RETURN a.fname , a.lname , a.gender ", {'lname':quer[2]})

                qactmoviesname = session.run("MATCH (a:actors)"
                                             "-[r:ACTED_CHARACTER]->(m:movies) WHERE a.lname = {lname}"
                                             " RETURN DISTINCT m.idmovies, m.title, m.year ORDER BY m.year DESC", {'lname':quer[2]})

                for record in qactorname:
                    print("First Name: %s \nLast Name: %s \nGender: %s\n" % (
                    record["a.fname"], record["a.lname"], record["a.gender"]))
                    tempDict = {
                        'First Name: ': record["a.fname"],
                        'Last Name: ': record["a.lname"],
                        'Gender: ': record["a.gender"]
                    }
                    diction.append(tempDict)
                for record in qactmoviesname:
                    print("Movie Id: %s \nTitle: %s \nYear: %s\n" % (
                    record["m.idmovies"], record["m.title"], record["m.year"]))
                    tempDict = {
                        'Movie Id: ': record["m.idmovies"],
                        'Title: ': record["m.title"],
                        'Year: ': record["m.year"]
                    }
                    diction.append(tempDict)

        else:

            qactorname = session.run("MATCH (a:actors) WHERE a.fname = {fname} AND a.lname = {lname}  "
                                     "RETURN a.fname , a.lname , a.gender ", {'fname': quer[2] ,'lname': quer[3]})

            qactmoviesname = session.run("MATCH (a:actors)"
                                         "-[r:ACTED_CHARACTER]->(m:movies) WHERE a.fname = {fname} AND a.lname = {lname}"
                                         " RETURN DISTINCT m.idmovies, m.title, m.year ORDER BY m.year DESC",
                                         {'fname': quer[2] ,'lname': quer[3]})

            for record in qactorname:
                print("First Name: %s \nLast Name: %s \nGender: %s\n" % (
                    record["a.fname"], record["a.lname"], record["a.gender"]))
                tempDict = {
                    'First Name: ': record["a.fname"],
                    'Last Name: ': record["a.lname"],
                    'Gender: ': record["a.gender"]
                }
                diction.append(tempDict)
            for record in qactmoviesname:
                print("Movie Id: %s \nTitle: %s \nYear: %s\n" % (
                    record["m.idmovies"], record["m.title"], record["m.year"]))
                tempDict = {
                    'Movie Id: ': record["m.idmovies"],
                    'Title: ': record["m.title"],
                    'Year: ': record["m.year"]
                }
                diction.append(tempDict)


    return diction
