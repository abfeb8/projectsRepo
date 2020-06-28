import sqlite3

conn = sqlite3.connect('database.db')
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
#             ctg TEXT
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
# c.execute("INSERT INTO match VALUES('Yuvraj',12,20,1,0,48,0,36,1,0,0,0)")
# c.execute("INSERT INTO match VALUES('Rahane',49,75,3,0,0,0,0,0,1,0,0)")
# c.execute("INSERT INTO match VALUES('Dhawan',32,35,4,0,0,0,0,0,0,0,0)")
# c.execute("INSERT INTO match VALUES('Dhoni',56,45,3,1,0,0,0,0,3,2,0)")
# c.execute("INSERT INTO match VALUES('Axar',8,4,2,0,48,2,35,1,0,0,0)")
# c.execute("INSERT INTO match VALUES('Pandya',42,36,3,3,30,0,25,0,1,0,0)")
# c.execute("INSERT INTO match VALUES('Jadega',18,10,1,1,60,3,50,2,1,0,1)")
# c.execute("INSERT INTO match VALUES('Kedar',65,60,7,0,24,0,24,0,0,0,0)")
# c.execute("INSERT INTO match VALUES('Ashwin',23,42,3,0,60,2,45,6,0,0,0)")
# c.execute("INSERT INTO match VALUES('Umesh',0,0,0,0,54,0,50,4,1,0,0)")
# c.execute("INSERT INTO match VALUES('Bumrah',0,0,0,0,60,2,49,1,0,0,0)")
# c.execute("INSERT INTO match VALUES('Bhuwaneshwar',15,12,2,0,60,1,46,2,0,0,0)")
# c.execute("INSERT INTO match VALUES('Rohit',46,65,5,1,0,0,0,0,1,0,0)")
# c.execute("INSERT INTO match VALUES('Kartick',29,42,3,0,0,0,0,0,2,0,1)")


# c.execute("INSERT INTO stats VALUES('Kohli',189,8257,28,43,120,'BAT')")
# c.execute("INSERT INTO stats VALUES('Yuvraj',86,3589,10,21,100,'BAT')")
# c.execute("INSERT INTO stats VALUES('Rahane',158,5435,11,31,100,'BAT')")
# c.execute("INSERT INTO stats VALUES('Dhawan',25,565,2,1,85,'AR')")
# c.execute("INSERT INTO stats VALUES('Dhoni',78,2573,3,19,75,'BAT')")
# c.execute("INSERT INTO stats VALUES('Axar',67,208,0,0,100,'BWL')")
# c.execute("INSERT INTO stats VALUES('Pandya',70,77,0,0,75,'BWL')")
# c.execute("INSERT INTO stats VALUES('Jadega',16,1,0,0,85,'BWL')")
# c.execute("INSERT INTO stats VALUES('Kedar',111,675,0,1,90,'BWL')")
# c.execute("INSERT INTO stats VALUES('Ashwin',136,1914,0,10,100,'AR')")
# c.execute("INSERT INTO stats VALUES('Umesh',296,9496,10,64,110,'WK')")
# c.execute("INSERT INTO stats VALUES('Bumrah',73,1365,0,8,60,'WK')")
# c.execute("INSERT INTO stats VALUES('Bhuwaneshwar',17,289,0,2,75,'AR')")
# c.execute("INSERT INTO stats VALUES('Rohit',304,8701,14,52,85,'BAT')")
# c.execute("INSERT INTO stats VALUES('Kartick',11,111,0,0,75,'AR')")
# *************************************************************


'''listing tables'''
c.execute("SELECT * FROM match")
# c.execute("SELECT * FROM teams")
# c.execute("SELECT * FROM stats")
print(c.fetchall())

conn.commit()
conn.close()
