from flask import Flask,jsonify,request
from __init__ import app, db
from flask import request

lusers = [
    {
        'lusername': 'dhruva',
        'lpasshint': 'Who is gonna be very succesful when their older',
        'lpassword': 'dhruva123',
        'points' : '100'
    },
    {
        'lusername': 'drishya',
        'lpasshint': 'Who made jv1 soccer team this year?',
        'lpassword': 'drishya123',
        'points' : '200'
    },
    {    
        'lusername': 'prasith',
        'lpasshint': 'Who had anger issues when he was younger',
        'lpassword': 'prasith123',
        'points' : '300'
    },
    {
        'lusername': 'vyaan',
        'lpasshint': 'Whos your favoirte person?',
        'lpassword': 'vyaan123',
        'points' : '400'
    },
    {
        'lusername': 'admin',
        'lpasshint': 'Who has most wins in the UFC all time before a champsionship fight?',
        'lpassword': 'adminabc',
        'points' : '500'
    },
    {
        'lusername': 'guest',
        'lpasshint': 'Whats the name of an account with no user?',
        'lpassword': 'guest123',
        'points' : '500'
    },
]

@app.route("/lusers", methods=["GET"])
def get_lusers():
    return jsonify(lusers)

@app.route("/api/check_lpassword", methods=["POST"])
def check_lpassword():
    lusername = request.args.get('lusername')
    points = request.args.get('points')
    print(lusername,points)
    print(request.get_json())
    lpassword = request.get_json()["lpassword"]
    for luser in lusers:
        if lusername == luser["lusername"] and points == luser["points"]:
            if lpassword == luser["lpassword"]:
                return jsonify({"result": "Correct"})
    return jsonify({"result": "Incorrect"})

@app.route('/api/loginuser')
def test():
    lusername = request.args.get('lusername')
    points = request.args.get('points')
    print(lusername,points)
    for luser in lusers:
        if lusername == luser["lusername"] and points == luser["points"]:
            response = {
                "luser": luser["luser"]
            }
            return jsonify(response)
    return '{ "Luser": "Not found" }'


if __name__ == '__main__':
    app.run()


class LoginUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lusername = db.Column(db.Text)
    lpasshint = db.Column(db.Text)
    lpassword = db.Column(db.Text)
    points = db.Column(db.Integer)
    def __repr__(self):
        return f'Luser: {self.luser}'
db.drop_all()
db.create_all()


def makedb():
    for luser in lusers:
        luser = LoginUser(lusername=luser["lusername"],points=int(luser["points"]),lpassword=luser["lpassword"],lpasshint=luser["lpasshint"])
        db.session.add(luser)
    db.session.commit()
makedb()
#print(LoginUser.query.all())