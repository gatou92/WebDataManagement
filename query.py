import psycopg2

try:
    conn = psycopg2.connect("dbname='movies' user='postgres' host='localhost' password='KostisT10@@@'")
except:
    print "I am unable to connect to the database"

cur = conn.cursor()

cur.execute("""SELECT '(' || m.year ||') ' || m.title AS full_title,
count(ai.character) AS num_of_character
FROM movies m JOIN acted_in ai ON ai.idmovies=m.idmovies
JOIN actors a ON a.idactors=ai.idactors
WHERE m.title LIKE '%Terminator%'
AND TYPE=3 GROUP BY m.year, m.title ORDER BY m.year, m.title""")

rows = cur.fetchall()

print "\nShow me the databases:\n"
for row in rows:
    print "   ", row[0]