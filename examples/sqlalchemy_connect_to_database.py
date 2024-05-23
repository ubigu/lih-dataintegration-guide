from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create an engine to connect to the existing database
engine = create_engine('sqlite:///esimerkki.db', echo=True)

# Create a base class for declarative class definitions
Base = declarative_base()

# Define a class representing our table
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"<User(name='{self.name}', age={self.age})>"

# Create a session class
Session = sessionmaker(bind=engine)

# Create a session
session = Session()

# Add some data
user1 = User(name='Markku', age=30)
user2 = User(name='Heli', age=25)
session.add(user1)
session.add(user2)
session.commit()

# Query the data
users = session.query(User).all()
for user in users:
    print(user)