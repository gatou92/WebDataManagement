def mongo_sc2(quer, db):
    diction=[]
    if quer[1].isdigit():
        #actor id is given

        #get actor info: first name, last name, gender
        cursorln = db.actors_acted_final.find({'idactors': quer[1]}).distinct("lname")
        cursorfn = db.actors_acted_final.find({'idactors': quer[1]}).distinct("fname")
        cursorge = db.actors_acted_final.find({'idactors': quer[1]}).distinct("gender")

        #create dictionary for actor info
        tempDict = {
            'First Name': cursorfn[0],
            'Last Name': cursorln[0],
            'Gender': cursorge[0]

        }
        # append the temporary dictionary to dict
        diction.append(tempDict)

        #get id movies of actor
        cursoract = db.actors_acted_final.find({'idactors': quer[1]}).distinct("idmovies")

        #for each id found
        for id in cursoract:

            #for
            cursort = db.movies_with_genres.find({'idmovies': id}).distinct("title")
            cursory = db.movies_with_genres.find({'idmovies': id}).distinct("year")
            tempDict = {
                    'Title': cursort[0],
                    'Year': cursory[0]

                }
            # append the temporary dictionary to dict
            diction.append(tempDict)

    else:
        if len(quer) == 3:
            if quer[1] == 'firstname':
                #first name is given

                #get actors with first name
                cnames=db.actors_acted_final.aggregate([
                    {"$match":{"fname":quer[2]}},
                    {"$group": {"_id":{"Gender":"$gender","First Name":"$fname", "Last Name":"$lname"}}},


                ])

                #append result to dictionary
                for c in cnames:
                    diction.append(c['_id'])


                #get id movies they played in
                cursorids = db.actors_acted_final.find({'fname': quer[2]}).distinct("idmovies")

                #for each id
                for id in cursorids:
                    #get title and year
                    cursort = db.movies_with_genres.find({'idmovies': id}).distinct("title")
                    cursory = db.movies_with_genres.find({'idmovies': id}).distinct("year")

                    #create dictionary for results
                    tempDict = {
                        'ID': id,
                        'Title': cursort[0],
                        'Year': cursory[0]

                    }

                    diction.append(tempDict)

            else:
                #last name is given

                #get actor info
                cnames = db.actors_acted_final.aggregate([
                    {"$match": {"lname": quer[2]}},
                    {"$group": {"_id": {"Gender": "$gender", "First Name": "$fname", "Last Name": "$lname"}}},

                ])

                #create dictionary
                for c in cnames:
                    print(c)
                    diction.append(c['_id'])

                #get id movies they played in
                cursorids = db.actors_acted_final.find({'lname': quer[2]}).distinct("idmovies")

                #for each id
                for id in cursorids:
                    #get title and year
                    cursort = db.movies_with_genres.find({'idmovies': id}).distinct("title")
                    cursory = db.movies_with_genres.find({'idmovies': id}).distinct("year")

                    #create dictionary
                    tempDict = {
                        'ID':id,
                        'Title': cursort[0],
                        'Year': cursory[0]

                    }
                    diction.append(tempDict)
        else:
            #first and last name given
            #get actor info
            cnames = db.actors_acted_final.aggregate([
                {"$match": {"fname": quer[2], "lname": quer[3] }},
                {"$group": {"_id": {"Gender": "$gender", "First Name": "$fname", "Last Name": "$lname"}}},

            ])

            #append results to dictionary
            for c in cnames:
                diction.append(c['_id'])

            #get idmovies they played in
            cursorids = db.actors_acted_final.find({'fname': quer[2], 'lname':quer[3]}).distinct("idmovies")

            #for each id
            for id in cursorids:
                #get movie info
                cursormv = db.movies_with_genres.find({'idmovies': id})

                #create dictionary with title and year
                for m in cursormv:
                    tempDict = {
                        'ID': id,
                        'Title': m['title'],
                        'Year': m['year']

                    }
                    # append the temporary dictionary to dict
                    diction.append(tempDict)




    return diction