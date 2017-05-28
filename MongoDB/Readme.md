MongoDB The JOIN problem: https://stackoverflow.com/questions/5841681/mongodb-normalization-foreign-key-and-joining

Some extra information: http://openmymind.net/Multiple-Collections-Versus-Embedded-Documents/#6

#####################################################################

Example for string partialmatch:                                    #
                                                                    #
cursor = db.movies.find({"title":{"$regex": u"Star Wars"}})         #
                                                                    #
for document in cursor:                                             #
    print(document)                                                 #
                                                                    #
#####################################################################

