def mongo_sc3(quer, db):
    diction=[]
    if quer[1].isdigit():
        #actorid is given

        #get actor info: last name, first name, gender
        cursorln = db.actors_acted_final.find({'idactors': quer[1]}).distinct("lname")
        cursorfn = db.actors_acted_final.find({'idactors': quer[1]}).distinct("fname")
        cursorge = db.actors_acted_final.find({'idactors': quer[1]}).distinct("gender")

        #create dictionary
        tempDict = {
            'First Name': cursorfn[0],
            'Last Name': cursorln[0],
            'Gender': cursorge[0]

        }
        # append the temporary dictionary to results
        diction.append(tempDict)

        #count the number of movies for that actor
        cursoract = db.actors_acted_final.aggregate([
                    {"$match":{"idactors":quer[1]}},
                    {"$group": {"_id": "null", "count": { "$sum": 1}}}
        ])

        #create dictionary with the number of movies
        for ac in cursoract:
            print ac['count']
            tempDict = {
                 'Number of Movies': ac['count']
                }


            # append the temporary dictionary to dict
            diction.append(tempDict)

    else:

        if len(quer) == 3:

            if quer[1] == 'firstname':
                #firstname is given

                #get results for that first name with group by
                cnames = db.actors_acted_final.aggregate([
                    {"$match": {"fname": quer[2]}},
                    {"$group": {"_id": {"Gender": "$gender", "First Name": "$fname", "Last Name": "$lname"},
                                "Number of Movies": { "$sum": 1}}},


                ])

                #append results to dictionary
                for c in cnames:
                    diction.append(c)

            else:
                #last name given
                cnames = db.actors_acted_final.aggregate([
                    {"$match": {"lname": quer[2]}},
                    {"$group": {"_id": {"Gender": "$gender", "First Name": "$fname", "Last Name": "$lname"},
                                "Number of Movies": {"$sum": 1}}},

                ])
                # append results to dictionary
                for c in cnames:
                    diction.append(c)

        else:
            # get results for that last name with group by
            cnames = db.actors_acted_final.aggregate([
            {"$match": {"fname": quer[2], "lname":quer[3]}},
            {"$group": {"_id": {"Gender": "$gender", "First Name": "$fname", "Last Name": "$lname"},
                        "Number of Movies": {"$sum": 1}}},

            ])
            # append results to dictionary
            for c in cnames:
                diction.append(c)


    return diction