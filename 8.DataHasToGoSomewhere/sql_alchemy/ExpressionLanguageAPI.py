import sqlalchemy as sa
conn = sa.create_engine('sqlite://')

# CREATE TABLE
meta = sa.MetaData()
zoo = sa.Table('zoo',meta,sa.Column('critter',sa.String),sa.Column('count',sa.Integer),sa.Column('damages',sa.Float))
meta.create_all(conn)
print(zoo)

# INSERT ROWS
insertStatement = zoo.insert(('bear',2,0.0))
conn.execute(insertStatement)
insertStatement = zoo.insert(('duck',10,0.0))
conn.execute(insertStatement)

# SELECT
selectStatement = zoo.select()
result = conn.execute(selectStatement)
rows = result.fetchall()
print(rows)