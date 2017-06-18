def mongo_sc4(quer, db):
    diction=[]
    print len(quer)
    if len(quer) == 4:
        # Then start and end year are given as input
        # collect movie id's in that year range with that genre
        cur = db.movies_with_genres.find({ "year": {"$gte": quer[2], "$lte": quer[3]},
                                                   "genre": quer[1]}).sort([ ("year", -1), ("title", -1)]).distinct("idmovies")

    else:
        # Then only one year is given as input
        # collect movie id's within that year and genre
        cur = db.movies_with_genres.find({ "year": quer[2] , "genre": quer[1]}).sort([ ("year",-1), ("title", -1) ]).distinct("idmovies")

    for c in cur:
        #for each id found

        #get the year of that movie
        cy = db.movies_with_genres.find({'idmovies': c}).distinct("year")

        #get the title of the movie
        ctit = db.movies_with_genres.find({'idmovies': c}).distinct("title")

        #create temporary dictionary with results
        tempDict = {
                'Title': ctit[0],
                'Year': cy[0]

        }
        #append the temporary dictionary to dict
        diction.append(tempDict)

    return diction
