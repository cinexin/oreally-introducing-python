import sqlite3
dbFile = '8.DataHasToGoSomewhere/sqlite/enterprise.db'
conn = sqlite3.connect(dbFile)

# CREATE TABLE
sqlSentence = '''CREATE TABLE zoo (critter  VARCHAR(20) PRIMARY KEY, count INT, damages FLOAT)'''
print(sqlSentence)
curs = conn.cursor()
curs.execute(sqlSentence)

# INSERT INTO
curs.execute('INSERT INTO zoo VALUES ("duck", 5, 0.0)')
curs.execute('INSERT INTO zoo VALUES ("bear", 2, 100.0)')
# insert using placeholders
ins = 'INSERT INTO zoo(critter, count, damages) VALUES (?,?,?)'
curs.execute(ins,('weasel',1,2000.0))

# SELECT...
curs.execute("SELECT * FROM zoo")
rows = curs.fetchall()
print(rows)
selectClause = "SELECT * FROM zoo ORDER BY count"
curs.execute(selectClause)
curs.fetchall()
selectClause = "SELECT * FROM zoo ORDER BY count DESC"
curs.execute(selectClause)
curs.fetchall()
complexSelectClase = '''SELECT * 
FROM zoo 
WHERE damages = (SELECT MAX(damages) FROM zoo)'''
curs.execute(complexSelectClase)
curs.fetchall()

# CLOSE cursor and connections...
curs.close()
conn.close()
