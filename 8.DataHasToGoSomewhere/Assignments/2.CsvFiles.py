'''
8.4. Use the csv module and its DictReader method to read books.csv to books var
Print values in books. Diud DictReader handle the quotes and commans in the second book's title?
'''
import csv
booksCsvFile = '8.DataHasToGoSomewhere/Assignments/books.csv'
with open(booksCsvFile,'rt') as fin:
    cin = csv.DictReader(fin)
    books = [row for row in cin]
    print(books)
'''
8.5. Create a CSV file called books.csv using the lines especified
'''
books = [
    {'title': 'The Weirdstone of Brisingamen', 'author': 'Alan Garner', 'year': 1960},
    {'title': 'Perdido Street Station', 'author': 'China Miéville', 'year': 2000},
    {'title': 'Thud!', 'author': 'Terry Pratchett', 'year': 2005},
    {'title': 'The Spellman Files', 'author': 'Lisa Lutz', 'year': 2007},
    {'title': 'Small Gods', 'author': 'Terry Pratchett', 'year': 1992},
]
booksCsvFile = '8.DataHasToGoSomewhere/Assignments/books.csv'
with open(booksCsvFile, 'wt', newline = '', encoding="utf-8") as fout:
    cout = csv.DictWriter(fout,['title','author','year'])
    cout.writeheader()
    cout.writerows(books)