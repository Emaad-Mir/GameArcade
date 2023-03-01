from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///login_users.db'
db = SQLAlchemy(app)

class LoginUser(db.Model):
 id = db.Column(db.Integer, primary_key=True)
 lusername = db.Column(db.Text)
 lpasshint = db.Column(db.Text)
 lpassword = db.Column(db.Text)

def __repr__(self):
 return f'Luser: {self.lusername}'

users = [
{'lusername': 'dhruva', 
'lpasshint': 'dhruva try to remember', 
'lpassword': 'dhruva123'},
{'lusername': 'drishya', 
'lpasshint': 'drishya try to remember', 
'lpassword': 'drishya123'},
{'lusername': 'prasith', 
'lpasshint': 'prasith try to remember', 
'lpassword': 'prasith123'},
{'lusername': 'vyaan', 
'lpasshint': 'vyaan try to remember', 
'lpassword': 'vyaan123'},
{'lusername': 'admin', 
'lpasshint': 'you really think you can get a hint for admin', 
'lpassword': 'adminabc'},
{'lusername': 'guest', 
'lpasshint': 'just try guest and some numbers', 
'lpassword': 'guest123'},
]

@app.route("/users", methods=["GET"])
def get_userss():
    return jsonify(users)

@app.route("/api/check_lpassword", methods=["POST"])
def check_lpassword():
 lusername = request.json.get('lusername')
 lpassword = request.json.get('lpassword')
 for user in users:
  if lusername == user["lusername"] and lpassword == user["lpassword"]:
         return jsonify({"result": "Correct"})
 return jsonify({"result": "Incorrect"})