import dbm
dbmFile = '8.DataHasToGoSomewhere/no_sql_dbs/definitions.db'
db = dbm.open(dbmFile,'c')
db['mustard'] = 'yellow'
db['ketchup'] = 'red'
db['pesto'] = 'green'

len(db)
print(db['pesto'])
db.close()

db = dbm.open(dbmFile,'r')
print(db['mustard'])
