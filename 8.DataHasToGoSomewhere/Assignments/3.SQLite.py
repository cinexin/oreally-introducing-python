'''
8.6
Use sqlite3 module to create a SQLite database called 'books.db'
Create a table called 'books' with fields:
- title (text)
- author (text)
- year (int)
'''

import sqlite3
dbFile = '8.DataHasToGoSomewhere/Assignments/books.db'
conn = sqlite3.connect(dbFile)
sqlSentence = '''CREATE TABLE books (title VARCHAR(255) PRIMARY KEY, author VARCHAR(255), year INT)'''
curs = conn.cursor()
curs.execute(sqlSentence)
deleteSentence = 'DELETE FROM books'
curs.execute(deleteSentence)


'''
8.7. Read books.csv file and insert its data into the book table
'''

import csv
booksFile = '8.DataHasToGoSomewhere/Assignments/books.csv'
with open(booksFile,'rt') as fin:
    cin = csv.DictReader(fin)
    for book in cin:
        print(book)
        insertBookSqlSentence = 'INSERT INTO books(title, author, year) VALUES (?,?,?)'
        curs.execute(insertBookSqlSentence, (book['title'], book['author'], book['year']))


'''
8.8. Select and print the title column for the book table in alphabetical order
'''    
curs.execute("SELECT title FROM books ORDER BY title ASC")
fetchedBooks = curs.fetchall()
print(fetchedBooks)


'''
8.9. Select and print all columns from the book table in order of publication
'''
curs.execute("SELECT * FROM books ORDER BY year ASC")
fetchedBooks = curs.fetchall()
print(fetchedBooks)