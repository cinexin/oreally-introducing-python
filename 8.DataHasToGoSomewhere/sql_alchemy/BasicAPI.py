import sqlalchemy as sa
# Create an "in-memory" database
conn = sa.create_engine('sqlite://')
# CREATE TABLE
createTableSentence = "CREATE TABLE zoo (critter VARCHAR(20) PRIMARY KEY, count INT, damages FLOAT)"
conn.execute(createTableSentence)

# INSERT ROWS
insTemplateSentence = "INSERT INTO zoo(critter, count, damages) VALUES(?,?,?)"
conn.execute(insTemplateSentence,'duck',10,0.0)
conn.execute(insTemplateSentence,'bear',2,1000.0)
conn.execute(insTemplateSentence,'weasel',1,2000.0)

# SELECT
rows = conn.execute("SELECT * FROM zoo")
print(rows)
for row in rows:
    print(row)