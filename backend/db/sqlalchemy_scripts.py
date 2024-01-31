from sqlalchemy import create_engine
from sqlalchemy.engine import URL

url = URL.create(
    drivername="postgresql",
    username="shaggy",
    host="localhost",
    database="rpgshelf"
)
engine = create_engine(url, echo=True)
connection = engine.connect()


from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.orm import declarative_base, relationship, backref
from datetime import datetime

Base = declarative_base()

class System(Base):
    __tablename__ = 'systems'

    gid = Column(Integer(), primary_key=True)
    system_name = Column(String(100), nullable=False, unique=True)
    rid = Column(Integer(), nullable=True, unique=True)
    system = Column(String(100))
    description = Column(Text)
    edition = Column(String(50), nullable = True)
    library = relationship('Book', backref='system')


class Book(Base):
    __tablename__ = 'library'
    
    bid = Column(Integer(), primary_key=True)
    brid = Column(Integer())
    book_title = Column(String(150))
    asset_type = Column(String(100))
    description = Column(Text)
    path = Column(String(200))
    image = Column(String(200))
    publisher = Column(String(200))
    designers = Column(String(200))
    artists = Column(String(200))
    producers = Column(String(200))
    year = Column(DateTime())

Base.metadata.create_all(engine)
