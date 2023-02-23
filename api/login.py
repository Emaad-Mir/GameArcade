from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'volumes:///sqlite.db' 
bcrypt = Bcrypt(app)
db = SQLAlchemy(app) 

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

db.drop_all()
db.create_all()

users = [
    {'username': 'user1', 'password': 'pass1'},
    {'username': 'user2', 'password': 'pass2'},
    {'username': 'user3', 'password': 'pass3'},
]

for user in users:
    hashed_password = bcrypt.generate_password_hash(user['password']).decode('utf-8')
    new_user = User(username=user['username'], password=hashed_password)
    db.session.add(new_user)

db.session.commit()
