def neo4j_sc3(quer, session):
    diction=[]

    if quer[1].isdigit():

        qactmoviesid = session.run("MATCH (a:actors)"
                                  "-[r:ACTED_CHARACTER]->(m:movies) WHERE a.idactors = {idactors}"
                                   " RETURN a.fname , a.lname, COUNT(DISTINCT m.idmovies)", {'idactors':int(quer[1])})

        for record in qactmoviesid:
          print("First Name: %s \nLast Name: %s \nNumber of Played Movies: %s \n" % (
          record["a.fname"], record["a.lname"], record["COUNT(DISTINCT m.idmovies)"]))
          tempDict = {
              'First Name: ': record["a.fname"],
              'Last Name: ': record["a.lname"],
              'Number of Played Movies: ': record["COUNT(DISTINCT m.idmovies)"]
          }
          diction.append(tempDict)

    else:
        if len(quer) == 3:
            if quer[1] == 'firstname':
                qshortactmoviesname = session.run("MATCH (a:actors)"
                                            "-[r:ACTED_CHARACTER]->(m:movies) WHERE a.fname = {fname} "
                                        " RETURN a.fname, a.lname, COUNT(DISTINCT m.idmovies)  ", {'fname':quer[2]})

                for record in qshortactmoviesname:
                    print("First Name: %s \nLast Name: %s \nNumber of Played Movies: %s \n" % (
                    record["a.fname"], record["a.lname"], record["COUNT(DISTINCT m.idmovies)"]))
                    tempDict = {
                        'First Name: ': record["a.fname"],
                        'Last Name: ': record["a.lname"],
                        'Number of Played Movies: ': record["COUNT(DISTINCT m.idmovies)"]
                    }
                    diction.append(tempDict)

            else:
                qshortactmoviesname = session.run("MATCH (a:actors)"
                                                  "-[r:ACTED_CHARACTER]->(m:movies) WHERE a.lname = {lname}"
                                                  " RETURN a.fname, a.lname, COUNT(DISTINCT m.idmovies)  ", {'lname':quer[2]})

                for record in qshortactmoviesname:
                    print("First Name: %s \nLast Name: %s \nNumber of Played Movies: %s \n" % (
                    record["a.fname"], record["a.lname"], record["COUNT(DISTINCT m.idmovies)"]))
                    tempDict = {
                        'First Name: ': record["a.fname"],
                        'Last Name: ': record["a.lname"],
                        'Number of Played Movies: ': record["COUNT(DISTINCT m.idmovies)"]
                    }
                    diction.append(tempDict)
        else:
            qshortactmoviesname = session.run("MATCH (a:actors)"
                                              "-[r:ACTED_CHARACTER]->(m:movies) WHERE a.fname = {fname} AND a.lname = {lname}"
                                              " RETURN a.fname, a.lname, COUNT(DISTINCT m.idmovies)  ",
                                              {'fname': quer[2] ,'lname': quer[3]})

            for record in qshortactmoviesname:
                print("First Name: %s \nLast Name: %s \nNumber of Played Movies: %s \n" % (
                    record["a.fname"], record["a.lname"], record["COUNT(DISTINCT m.idmovies)"]))
                tempDict = {
                    'First Name: ': record["a.fname"],
                    'Last Name: ': record["a.lname"],
                    'Number of Played Movies: ': record["COUNT(DISTINCT m.idmovies)"]
                }
                diction.append(tempDict)



    return diction
