from sqlalchemy import create_engine, MetaData, Integer, String, DateTime, Text, ARRAY, ForeignKey
from sqlalchemy.engine import URL
from sqlalchemy.orm import DeclarativeBase, relationship, backref, Mapped, mapped_column, sessionmaker
from datetime import datetime
from typing import List

url = URL.create(
    drivername="postgresql",
    username="shaggy",
    host="localhost",
    database="rpgshelf"
)
engine = create_engine(url, echo=True)
connection = engine.connect()
metadata_obj = MetaData()

Session = sessionmaker(bind=engine)
session = Session()



class Base(DeclarativeBase):
    pass

class System(Base):
    __tablename__ = 'systems'
    gid = mapped_column(Integer(), primary_key=True)
    system_name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    rid: Mapped[int] = mapped_column(Integer(), unique=True)
    system: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(Text)
    edition: Mapped[str] = mapped_column(String(50), nullable = True)
    library: Mapped[List["Book"]] = relationship()
    
    def __repr__(self):
        return f'{self.system_name}'


class Book(Base):
    __tablename__ = 'library'    
    bid = mapped_column(Integer(), primary_key=True)
    system_rid: Mapped[int] = mapped_column(ForeignKey('systems.rid'))
    # system: Mapped["System"] = relationship(back_populates="library")
    brid: Mapped[int] = mapped_column(Integer(), nullable=False, unique=True)
    book_title: Mapped[str] = mapped_column(String(150))
    # asset_type: Mapped[str] = mapped_column(String(100), nullable=True)
    description: Mapped[str] = mapped_column(Text)
    # path: Mapped[str] = mapped_column(String(200), nullable=True)
    # image: Mapped[str] = mapped_column(String(200), nullable=True)
    publisher: Mapped[list] = mapped_column(ARRAY(String(200)))
    designers: Mapped[list] = mapped_column(ARRAY(String(200)))
    artists: Mapped[list] = mapped_column(ARRAY(String(200)))
    producers: Mapped[list] = mapped_column(ARRAY(String(200)))
    year: Mapped[str] = mapped_column(String(10), nullable=True)
    
    def __repr__(self):
        return f'Node {self.book_title}'

def createTables() :
    Base.metadata.create_all(engine)
