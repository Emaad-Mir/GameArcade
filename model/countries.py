""" database dependencies to support sqliteDB examples """
from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash


''' Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along '''

# Define the Post class to manage actions in 'posts' table,  with a relationship to 'users' table
class Post2(db.Model):
    __tablename2__ = 'countrytable'

    # Define the Notes schema
    id = db.Column(db.Integer, primary_key=True)
    note = db.Column(db.Text, unique=False, nullable=False)
    image = db.Column(db.String, unique=False)
    # Define a relationship in Notes Schema to userID who originates the note, many-to-one (many notes to one user)
    countryID = db.Column(db.Integer, db.ForeignKey('countries.id'))

    # Constructor of a Notes object, initializes of instance variables within object
    def __init__(self, id, note, image):
        self.countryID = id
        self.note = note
        self.image = image

    # Returns a string representation of the Notes object, similar to java toString()
    # returns string
    def __repr__(self):
        return "Notes(" + str(self.id) + "," + self.note + "," + str(self.countryID) + ")"

    # CRUD create, adds a new record to the Notes table
    # returns the object added or None in case of an error
    def create(self):
        try:
            # creates a Notes object from Notes(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Notes table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None

    # CRUD read, returns dictionary representation of Notes object
    # returns dictionary
    def read(self):
        # encode image
        path = app.config['UPLOAD_FOLDER']
        file = os.path.join(path, self.image)
        file_text = open(file, 'rb')
        file_read = file_text.read()
        file_encode = base64.encodebytes(file_read)
        
        return {
            "id": self.id,
            "countryID": self.countryID,
            "note": self.note,
            "image": self.image,
            "base64": str(file_encode)
        }


# Define the User class to manage actions in the 'users' table
# -- Object Relational Mapping (ORM) is the key concept of SQLAlchemy
# -- a.) db.Model is like an inner layer of the onion in ORM
# -- b.) User represents data we want to store, something that is built on db.Model
# -- c.) SQLAlchemy ORM is layer on top of SQLAlchemy Core, then SQLAlchemy engine, SQL
class Countries(db.Model):
    __tablename2__ = 'countries'  # table name is plural, class name is singular

    # Define the User schema with "vars" from object
    _cid = db.Column(db.Integer, primary_key=True)
    _name = db.Column(db.String(255), unique=False, nullable=False)
    # Defines a relationship between User record and Notes table, one-to-many (one user to many notes)
    posts = db.relationship("Post2", cascade='all, delete', backref='users', lazy=True)

    # constructor of a User object, initializes the instance variables within object (self)
    def __init__(self, name, cid):
        self._name = name 
        self._cid = cid# variables with self prefix become part of the object, 
    # a name getter method, extracts name from object
    @property
    def name(self):
        return self._name
    
    # a setter function, allows name to be updated after initial object creation
    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def cid(self):
        return self._cid
    
    # a setter function, allows name to be updated after initial object creation
    @name.setter
    def cid(self, cid):
        self._cid = cid

    # output content using str(object) in human readable form, uses getter
    # output content using json dumps, this is ready for API response
    def __str__(self):
        return json.dumps(self.read())

    # CRUD create/add a new record to the table
    # returns self or None on error
    def create(self):
        #try:
            # creates a person object from User(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Users table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        #except IntegrityError:
         #   db.session.remove()
          #  return None

    # CRUD read converts self to dictionary
    # returns dictionary
    def read(self):
        return {
            "cid": self.cid,
            "name": self.name
        }
    #"posts": [post.read() for post in self.posts]
    # CRUD update: updates user name, password, phone
    # returns self

    def update(self, name = "", cid = -1):
        """only updates values with length"""
        self.name = name
        self.cid = cid
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return {"message":f"deleted {self}"}
"""Database Creation and Testing """


# Builds working data for testing
def initCountries():
    """Create database and tables"""
    db.create_all()
    """Tester data for table"""
    #u1 = Countries(name='test',cid = 0)

    countries = []

    """Builds sample user/note(s) data"""
    for country in countries:
        try:
            '''add a few 1 to 4 notes per user'''
            for num in range(randrange(1, 4)):
                note = "#### " + country.name + " note " + str(num) + ". \n Generated by test data."
                country.posts.append(Post2(id=country.id, note=note, image='ncs_logo.png'))
            '''add user/post data to table'''
            country.create()
        except IntegrityError:
            '''fails with bad or duplicate data'''
            db.session.remove()
            print(f"Records exist, duplicate email, or error: {country.id}")
            