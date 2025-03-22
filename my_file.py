import sqlite3
con = sqlite3.connect("./data/sample.db")

cur = con.cursor()

cur.execute("PRAGMA table_info(your_table_name)")

rows = cur.fetchall()

print(rows.__dict__)

# cur.execute("CREATE TABLE movie(title, year, score)")

# cur.execute("""
#     INSERT INTO movie VALUES
#         ('Monty Python and the Holy Grail', 1975, 8.2),
#         ('And Now for Something Completely Different', 1971, 7.5)
# """)

print ('Hello, world!')
