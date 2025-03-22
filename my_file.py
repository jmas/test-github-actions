import sqlite3
con = sqlite3.connect("./data/sample.db")

cur = con.cursor()

cur.execute("SELECT * FROM movie")

rows = cur.fetchall()

print (len(rows))

cur.execute("CREATE TABLE movie(title, year, score)")

cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")

print ('Hello, world!')
