import sqlalchemy as sa
import sqlalchemy.engine.url as url
'''
8.10
Use the sqlalchemy module to connecto to the sqlite3 database books.db
Select and print title column from book table in alphabetical order
'''
pathToDatabase = 'sqlite:///books.db'
conn = sa.create_engine(pathToDatabase, echo = True)
rows = conn.execute("SELECT * FROM books")
for row in rows:
    print(row)