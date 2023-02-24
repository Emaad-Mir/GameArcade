import requests
from flask import Flask

common_passwords = ['password', '123456', 'qwerty', 'abc123', 'admin']

@app.route('/api/passwords')
def passwords():
    return jsonify(common_passwords)

if name == 'main':
    app.run()
print("dhruva is sexy")









from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError


class Tic(db.Model):
    __tablename__ = 'tics'  # table name is plural, class name is singular

    # Define the User schema with "vars" from object
    id = db.Column(db.Integer, primary_key=True)
    _name = db.Column(db.String(255), unique=False, nullable=False)
    _score = db.Column(db.String(255), unique=False, nullable=False)


    # Defines a relationship between User record and Notes table, one-to-many (one user to many notes)

    # constructor of a User object, initializes the instance variables within object (self)
    def __init__(self, name, score):
        self._name = name    # variables with self prefix become part of the object, 
        self._score = score

    # a name getter method, extracts name from object
    @property
    def name(self):
        return self._name
    
    # a setter function, allows name to be updated after initial object creation
    @name.setter
    def name(self, name):
        self._name = name

    # a score getter method, extracts name from object
    @property
    def score(self):
        return self._score
    
    # a setter function, allows score to be updated after initial object creation
    @name.setter
    def name(self, score):
        self._score = score
    

    
    
    
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
        }

    # CRUD update: updates user name, password, phone
    # returns self
    def update(self, name, score):
        """only updates values with length"""
        if len(name) > 0:
            self.name = name
        if score > 0:
            self._score = score
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
    tic1 = Tic(name="Vyaan", score = "20")
    tic2 = Tic(name="Dhruva", score = "5")
    tic3 = Tic(name="Nikhil", score = "15")
    tic4 = Tic(name="Drishya", score = "4")
    tic5 = Tic(name="Tai", score = "18")



    tics = [tic1, tic2, tic3, tic4, tic5]

    """Builds sample user/note(s) data"""
    for tic in tics:
        try:
            tic.create()
        except IntegrityError:
            '''fails with bad or duplicate data'''
            db.session.remove()
            print(f"Records exist, duplicate id, or error: {tic.id}")
            