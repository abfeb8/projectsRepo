import sqlite3

conn = sqlite3.connect('./database.db')
c = conn.cursor()

'''Crating Tables'''
# c.execute('''
#           CREATE TABLE match(
#             Name TEXT,
#             Score INTEGER,
#             Faced INTEGER,
#             Fours INTEGER,
#             Sixes INTEGER,
#             Bowled INTEGER,
#             Maiden INTEGER,
#             Given INTEGER,
#             Wkts INTEGER,
#             Catches INTEGER,
#             Stumping INTEGER,
#             RO INTEGER
#             )
#             ''')

# ************************************************************

# c.execute('''
#           CREATE TABLE stats(
#             Player TEXT,
#             Matches INTEGER,
#             Run INTEGER,
#             '100s' INTEGER,
#             '50s' INTEGER,
#             Value INTEGER,
#             ctg INTEGER
#             )
#             ''')

# *************************************************************

# c.execute('''
#           CREATE TABLE teams(
#             Name TEXT,
#             Player TEXT,
#             Value INTEGER
#             )
#             ''')

# *************************************************************

'''Entering values into tables'''
# c.execute("INSERT INTO match VALUES('Rahane',49,75,3,0,0,0,0,0,0,0,1)")

# *************************************************************


'''listing tables'''
# c.execute("SELECT * FROM match")
# c.execute("SELECT * FROM teams")
# c.execute("SELECT * FROM stats")
# print(c.fetchall())

conn.commit()
conn.close()
