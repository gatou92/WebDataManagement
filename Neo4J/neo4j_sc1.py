def neo4j_sc1(quer, session):
    diction=[]

    if quer[1].isdigit():
        qmovies = session.run("MATCH (a:movies) WHERE a.idmovies = {id} "
                              "RETURN a.idmovies , a.title , a.year ", {'id':int(quer[1])})

        qseries = session.run("MATCH (a:movies) "
                             "-[r:RELATED_TO_SERIES]->(b:series) WHERE a.idmovies = {idm} "
                            "RETURN b.idseries, b.name, b.season, b.number", {'idm':int(quer[1])})

        qgenres = session.run("MATCH (a:movies) "
                            "-[r:MOVIE_GENRE]->(b:genres) WHERE a.idmovies = {idm}"
                            " RETURN b.idgenres, b.genre", {'idm':int(quer[1])})

        qkeywords = session.run("MATCH (a:movies) "
                             "-[r:MOVIE_KEYWORD]->(b:keywords) WHERE a.idmovies = {idm}"
                             "RETURN b.idkeywords, b.keyword", {'idm':int(quer[1])})

        qactors = session.run("MATCH (a:actors)-[r:ACTED_CHARACTER]->(b:movies) WHERE b.idmovies = {idm}"
                          "RETURN a.idactors, a.fname, a.lname, a.gender, r.billing_position, r.character ORDER BY r.billing_position ASC ", {'idm':int(quer[1])})

        for record in qmovies:
            print("id: %s \nTitle: %s \nYear: %s\n" % (record["a.idmovies"], record["a.title"], record["a.year"]))
            tempDict={
                'ID: ': record["a.idmovies"],
                'Title: ': record["a.title"],
                'Year: ': record["a.year"]
            }
            diction.append(tempDict)

        for record in qseries:
            print("Name: %s \nSeason: %s \nEpisode: %s\n" % (record["b.name"], record["b.season"], record["b.number"]))
            tempDict = {
                'Name: ': record["b.name"],
                'Season: ': record["b.season"],
                'Episode: ': record["b.number"]
            }
            diction.append(tempDict)

        for record in qgenres:
            print("Genre: %s \n" % (record["b.genre"]))
            tempDict = {
                'Gerne: ': record["b.genre"]
            }
            diction.append(tempDict)
        for record in qkeywords:
            print("Keywords: %s \n" % (record["b.keyword"]))
            tempDict = {
                'Keywords: ': record["b.keyword"]
            }
            diction.append(tempDict)
        for record in qactors:
            print("First name: %s \nLast name: %s \nGender: %s \nCharacter: %s \nBilling position: %s\n" % (
            record["a.fname"], record["a.lname"], record["a.gender"], record["r.character"], record["r.billing_position"]))
            tempDict = {
                'First name: ': record["a.fname"],
                'Last name: ': record["a.lname"],
                'Gender: ': record["a.gender"],
                'Character: ': record["r.character"],
                'Billing Position: ': record["r.billing_position"]
            }
            diction.append(tempDict)

    else:
        qmovies = session.run("MATCH (a:movies) WHERE a.title =~ {ptitle}   "
                              "RETURN a.idmovies , a.title , a.year ", {'ptitle':'.*' + quer[1] + '.*'})

        qseries = session.run("MATCH (a:movies) "
                              "-[r:RELATED_TO_SERIES]->(b:series)  WHERE a.title =~ {ptitle}"
                              "RETURN b.idseries, b.name, b.season, b.number ", {'ptitle':'.*' + quer[1] + '.*'})

        qgenres = session.run("MATCH (a:movies ) "
                              "-[r:MOVIE_GENRE]->(b:genres) WHERE a.title =~ {ptitle}"
                              " RETURN DISTINCT b.idgenres, b.genre", {'ptitle':'.*' + quer[1] + '.*'})

        qkeywords = session.run("MATCH (a:movies ) "
                                "-[r:MOVIE_KEYWORD]->(b:keywords) WHERE a.title =~ {ptitle}"
                                "RETURN DISTINCT b.idkeywords, b.keyword", {'ptitle':'.*' + quer[1] + '.*'})

        qactors = session.run("MATCH (a:actors )-[r:ACTED_CHARACTER]->(b:movies ) WHERE b.title =~ {ptitle}"
                              "RETURN a.idactors, a.fname, a.lname, a.gender, r.billing_position, r.character ORDER BY r.billing_position ASC ", {'ptitle':'.*' + quer[1] + '.*'})

        for record in qmovies:
            print("id: %s \nTitle: %s \nYear: %s\n" % (record["a.idmovies"], record["a.title"], record["a.year"]))
            tempDict={
                'ID: ': record["a.idmovies"],
                'Title: ': record["a.title"],
                'Year: ': record["a.year"]
            }
            diction.append(tempDict)

        for record in qseries:
            print("Name: %s \nSeason: %s \nEpisode: %s\n" % (record["b.name"], record["b.season"], record["b.number"]))
            tempDict = {
                'Name: ': record["b.name"],
                'Season: ': record["b.season"],
                'Episode: ': record["b.number"]
            }
            diction.append(tempDict)
        for record in qgenres:
            print("Genre: %s \n" % (record["b.genre"]))
            tempDict = {
                'Gerne: ': record["b.genre"]
            }
            diction.append(tempDict)
        for record in qkeywords:
            print("Keywords: %s \n" % (record["b.keyword"]))
            tempDict = {
                'Keywords: ': record["b.keyword"]
            }
            diction.append(tempDict)
        for record in qactors:
            print("First name: %s \nLast name: %s \nGender: %s \nCharacter: %s \nBilling position: %s\n" % (
                record["a.fname"], record["a.lname"], record["a.gender"], record["r.character"],
                record["r.billing_position"]))
            tempDict = {
                'First name: ': record["a.fname"],
                'Last name: ': record["a.lname"],
                'Gender: ': record["a.gender"],
                'Character: ': record["r.character"],
                'Billing Position: ': record["r.billing_position"]
            }
            diction.append(tempDict)


    return diction