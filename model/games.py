from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError


class Game(db.Model):
    __tablename__ = 'games'  # table name is plural, class name is singular

    # Define the User schema with "vars" from object
    id = db.Column(db.Integer, primary_key=True)
    _name = db.Column(db.String(255), unique=False, nullable=False)
    _date = db.Column(db.Date)
    _desc = db.Column(db.String(255), unique=False, nullable=False)
    _link = db.Column(db.String(255), unique=False, nullable=False)


    # Defines a relationship between User record and Notes table, one-to-many (one user to many notes)

    # constructor of a User object, initializes the instance variables within object (self)
    def __init__(self, name, date_made ,desc="",link=""):
        self._name = name    # variables with self prefix become part of the object, 
        self._date = date_made
        self._desc = desc
        self._link = link

    # a name getter method, extracts name from object
    @property
    def name(self):
        return self._name
    
    # a setter function, allows name to be updated after initial object creation
    @name.setter
    def name(self, name):
        self._name = name
    

    @property
    def desc(self):
        return self._desc
    
    # a setter function, allows name to be updated after initial object creation
    @desc.setter
    def desc(self, desc):
        self._desc = desc
    

    @property
    def link(self):
        return self._link
    
    # a setter function, allows name to be updated after initial object creation
    @link.setter
    def link(self, link):
        self._link = link
    
    # dob property is returned as string, to avoid unfriendly outcomes
    @property
    def date(self):
        true_date = date.today()
        dob_string = true_date.strftime("%m-%d-%Y")
        return dob_string
    
    # dob should be have verification for type date
    @date.setter
    def date(self, date_made):
        self._date = date_made
    
    # output content using str(object) in human readable form, uses getter
    # output content using json dumps, this is ready for API response
    def __str__(self):
        return json.dumps(self.read())

    # CRUD create/add a new record to the table
    # returns self or None on error
    def create(self):
        try:
            # creates a person object from User(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Users table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None

    # CRUD read converts self to dictionary
    # returns dictionary
    def read(self):
        return {
            "id": self.id,
            "name": self.name,
            "desc": self.desc,
            "date": self.date,
            "link": self.link
        }

    # CRUD update: updates user name, password, phone
    # returns self
    def update(self, name="", desc=""):
        """only updates values with length"""
        if len(name) > 0:
            self.name = name
        if len(desc) > 0:
            self.desc = desc
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None


"""Database Creation and Testing """


# Builds working data for testing
def initGames():
    """Create database and tables"""
    db.create_all()
    """Tester data for table"""
    g5 = Game(name="Hangman", desc="Guess the word in 7 tries!", date_made=date(2023, 1, 23),link="https://emaad-mir.github.io/GamesArcade/hangman")


    games = [g5]

    """Builds sample user/note(s) data"""
    for game in games:
        try:
            game.create()
        except IntegrityError:
            '''fails with bad or duplicate data'''
            db.session.remove()
            print(f"Records exist, duplicate email, or error: {game.uid}")
            