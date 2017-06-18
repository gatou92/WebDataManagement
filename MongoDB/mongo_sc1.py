def mongo_sc1(quer, db):

    #diction to append results
    diction=[]

    if quer[1].isdigit():
        #then movie id is given as argument
        #get title of movie
        cursortitle = db.movies_with_genres.find({'idmovies': quer[1]}).distinct("title")  # krataei mono to title doc sketo oxi doc[title]

        #get year of movie
        cursoryear = db.movies_with_genres.find({'idmovies': quer[1]}).distinct("year")

        #create dictionary to print the movie info
        tempDict = {
                'ID': quer[1],
                'Title': cursortitle[0],
                'Year': cursoryear[0]
            }
            # append the temporary dictionary to dict
        diction.append(tempDict)

        #get series names
        cursorseries = db.series.find({'idmovies': quer[1]}).distinct("name")

        #create dictionary for series
        for doc in cursorseries:
            print(doc)
            tempDict = {
                'Series Name': doc

            }
            # append the temporary dictionary to dict
            diction.append(tempDict)

        #get genres
        cursorgenre = db.movies_with_genres.find({'idmovies': quer[1]}).distinct("genre")

        #create dictionary for genres
        for doc in cursorgenre:
            print(doc)
            tempDict = {
                'Genre': doc
            }
            # append the temporary dictionary to dict
            diction.append(tempDict)

        #get keywords keywords for movie
        cursorkeys = db.movies_and_keywords.find({'idmovies': quer[1]}).distinct("keyword")

        #create dictionary for keywords
        for doc in cursorkeys:
            print(doc)
            tempDict = {
                    'Keyword': doc

                }
            # append the temporary dictionary to dict
            diction.append(tempDict)

        #get actors
        cursoract = db.actors_acted_final.aggregate(
            [
                {"$match": {"idmovies": quer[1]}},
                {"$group": {"_id": { "character": "$character", "Last Name":"$lname",
                "First Name":"$fname", "Gender":"$gender", "Billing Position":"$billing_position" }}},
                {"$sort": {"billing_position": -1}}
            ])

        #create dictionary for actors
        for ac in cursoract:
            print (ac)
            diction.append(ac['_id'])
    else:
        #movie title is given as argument

        #get id's for all partially matched titles
        cursor = db.movies_with_genres.find({"title": {"$regex": quer[1]}}).distinct("idmovies")

        #for each movie id found
        for document in cursor:
            print(document)

            #get title of movie
            cursort = db.movies_with_genres.find({'idmovies': document}).distinct("title")

            #get year of movie
            cursory = db.movies_with_genres.find({'idmovies': document}).distinct("year")

            #create dictionary to append results
            tempDict = {
                'ID': document,
                'Title': cursort[0],
                'Year': cursory[0]

            }
            diction.append(tempDict)

            #get series name of movie
            cursors = db.series.find({'idmovies': document}).distinct("name")

            #create dictionary for series
            for doc in cursors:
                print(doc)
                tempDict = {
                    'Series Name': doc

                }
                # append the temporary dictionary to dict
                diction.append(tempDict)

            #get genres of movie
            cursorgenre = db.movies_with_genres.find({'idmovies': document}).distinct("genre")

            #create dictionary for genres
            for doc in cursorgenre:
                print(doc)
                tempDict = {
                    'Genre': doc
                    }
                # append the temporary dictionary to dict
                diction.append(tempDict)

            #get keywords of movie
            cursorkeys = db.movies_and_keywords.find({'idmovies': document}).distinct("keyword")

            #create dictionary for keywords
            for doc in cursorkeys:
                print(doc)
                tempDict = {
                        'Keyword': doc

                }

                diction.append(tempDict)

            #get actors of movie
            cursoract = db.actors_acted_final.aggregate(
            [
            {"$match": {"idmovies": document}},
            {"$group": {"_id": {"character": "$character", "Last Name": "$lname",
            "First Name": "$fname", "Gender": "$gender", "Billing Position": "$billing_position"}}},
            {"$sort": {"billing_position": -1}}

                    ])

            #create dictionary for actors
            for doc in cursoract:
                print(doc)
                diction.append(doc['_id'])





    return diction