from flask import Flask, jsonify
from__init__ import app, db 
from flask import request
app = Flask(name)

common_passwords = ['password', '123456', 'qwerty', 'abc123', 'admin']

@app.route('/api/passwords')
def passwords():
    return jsonify(common_passwords)

if name == 'main':
    app.run()