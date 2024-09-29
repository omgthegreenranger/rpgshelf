from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from base import db

class System(db.Model) :
    name = db.Column(db.String(255), unique=False, nullable=False)
    lsid = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    rid = db.Column(db.Integer, unique=False, nullable=False)
    library = db.Column(db.String(255))
    system = db.Column(db.String(255))
    description = db.Column(db.Text, nullable=True)
    image = db.Column(db.String(80))
    thumbnail = db.Column(db.String(80))

    def __repr__(self):
        return '<Post %r>' % self.name


class Library(db.Model):
    rid = db.Column(db.Integer, unique=False, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    lbid = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    system_lsid = db.Column(db.Integer, db.ForeignKey('system.lsid'))
    series = db.Column(db.String(80))
    series_number= db.Column(db.Integer)
    publisher = db.Column(db.Text)
    designers = db.Column(db.Text)
    artists = db.Column(db.Text)
    producers = db.Column(db.Text)
    year = db.Column(db.Integer)
    description = db.Column(db.Text)
    image = db.Column(db.String(80))
    thumbnail = db.Column(db.String(80))

    def __repr__(self):
        return '<Post %r>' % self.title
