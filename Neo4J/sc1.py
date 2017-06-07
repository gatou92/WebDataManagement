from neo4j.v1 import GraphDatabase, basic_auth

driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", "1234"))
session = driver.session()



qmovies = session.run("MATCH (a:movies) WHERE a.idmovies = {idmovies} "
                     "RETURN a.idmovies , a.title , a.year ",
                      {"idmovies": 3})


qseries = session.run("MATCH (a:movies {idmovies:3}) "
                      "-[r:RELATED_TO_SERIES]->(b:series)"
                      "RETURN b.idseries, b.name, b.season, b.number")


qgenres = session.run("MATCH (a:movies {idmovies:3}) "
                      "-[r:MOVIE_GENRE]->(b:genres)"
                      " RETURN b.idgenres, b.genre")


qkeywords = session.run("MATCH (a:movies {idmovies:3}) "
                        "-[r:MOVIE_KEYWORD]->(b:keywords)"
                        "RETURN b.idkeywords, b.keyword")


qactors = session.run("MATCH (a:actors)-[r:ACTED_CHARACTER]->(b:movies {idmovies:3} ) "
                      "RETURN a.idactors, a.fname, a.lname, a.gender, r.billing_position, r.character ORDER BY r.billing_position ASC ")




for record in qmovies:
     print("id: %s \nTitle: %s \nYear: %s\n"% (record["a.idmovies"], record["a.title"], record["a.year"]))
for record in qseries:
     print("Name: %s \nSeason: %s \nEpisode: %s\n"% (record["b.name"], record["b.season"], record["b.number"]))
for record in qgenres:
     print("Genre: %s \n"% (record["b.genre"]))
for record in qkeywords:
     print("Keywords: %s \n"% (record["b.keyword"]))
for record in qactors:
     print("First name: %s \nLast name: %s \nGender: %s \nCharacter: %s \nBilling position: %s\n"% (record["a.fname"], record["a.lname"], record["a.gender"], record["r.character"], record["r.billing_position"]))




session.close()