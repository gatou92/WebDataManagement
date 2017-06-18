def mongo_sc5(quer, db):
    diction = []

    #get all genres
    cursor_genres = db.movies_with_genres.find({}).distinct("genre")

    if len(quer) == 3:
        # start_year and end_year given as argument for the query | |

        for g in cursor_genres:
            #for each genre

            #count all movies with that genre between the years
            cursoract = db.movies_with_genres.aggregate([
                {"$match": {"genre": g, "year": {"$gte": quer[1], "$lte": quer[2]}}},
                {"$group": {"_id": "null", "count": {"$sum": 1}}}
            ])

            for c in cursoract:
                #create dictionary with the results
                tempDict = {
                'Genre': g,
                'Number of Movies': c['count']
                }
                diction.append(tempDict)

    else:
        # only start_year given as argument for the query
        for g in cursor_genres:
        #for each genre

            # count all movies with that genre and that year
            cursoract = db.movies_with_genres.aggregate([
                {"$match": {"genre": g, "year": quer[1]}},
                {"$group": {"_id": "null", "count": {"$sum": 1}}}
            ])

            for c in cursoract:
                # create dictionary with the results
                tempDict = {
                'Genre': g,
                'Number of Movies': c['count']
                }
                diction.append(tempDict)

    return diction