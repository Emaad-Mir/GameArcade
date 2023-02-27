from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError


class Word(db.Model):
    __tablename__ = 'words'  # table name is plural, class name is singular

    # Define the User schema with "vars" from object
    id = db.Column(db.Integer, primary_key=True)
    _word = db.Column(db.String(255), unique=True, nullable=False)
   


    # Defines a relationship between User record and Notes table, one-to-many (one user to many notes)

    # constructor of a User object, initializes the instance variables within object (self)
    def __init__(self, word):
        self._word = word    # variables with self prefix become part of the object, 
       
    # a name getter method, extracts name from object
    @property
    def word(self):
        return self._word
    
    # a setter function, allows name to be updated after initial object creation
    @word.setter
    def word(self, word):
        self._word = word
    
        
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
            "word": self.word,
        }

    # CRUD update: updates user name, password, phone
    # returns self
    def update(self, word = ""):
        """only updates values with length"""
        if len(word) > 0:
            self.word = word
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
def initWords():
    with app.app_context():
        """Create database and tables"""
    db.create_all()
    """Tester data for table"""
    w1 = Word(word="Candy")


    words = [w1]

    """Builds sample user/note(s) data"""
    for word in words:
        try:
            word.create()
        except IntegrityError:
            '''fails with bad or duplicate data'''
            db.session.remove()
            print(f"Records exist, duplicate email, or error: {word.word}")
            