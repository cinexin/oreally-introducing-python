import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
conn = sa.create_engine('sqlite:///zoo.db')

# Define zoo model class
Base = declarative_base()
class Zoo(Base):
    __tablename__ = 'zoo'
    critter = sa.Column('critter', sa.String, primary_key = True)
    count = sa.Column('count', sa.Integer)
    damages = sa.Column('damages', sa.Float)
    
    def __init__(self,critter,count,damages, extend_existing=True):
        self.critter = critter
        self.count = count
        self.damages = damages
    
    def __repr__(self):
        return "<Zoo({} {} {})>".format(self.critter,self.count,self.damages)
    
# The following line magically creeates the database and table
Base.metadata.create_all(conn)

# Now, we can insert data the same way we create Python objects
duck = Zoo('duck',10,0.0)
bear = Zoo('bear',2,1000.0)
weasel = Zoo('weasel',1,2000.0)
print(duck)
print(bear)
print(weasel)

# Then we flush it into a physical database...
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=conn)
session = Session()
session.add(duck)
session.add_all([bear,weasel])
# this will create a 'zoo.db' physical database file
session.commit()
