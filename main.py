import threading

# import "packages" from flask
from flask import render_template  # import render_template from "public" flask libraries

# import "packages" from "this" project
from __init__ import app  # Definitions initialization
import model.jeopardy
from model.jokes import initJokes
from model.users import initUsers
from model.games import initGames
from model.words import initWords
from model.countries import initCountries


# setup APIs
from api.covid import covid_api # Blueprint import api definition
from api.joke import joke_api # Blueprint import api definition
from api.user import user_api # Blueprint import api definition
from api.game import game_api # Blueprint import api definition
from api.word import word_api
from api.country import country_api

import requests

# setup App pages
from projects.projects import app_projects # Blueprint directory import projects definition

# register URIs
app.register_blueprint(joke_api) # register api routes
app.register_blueprint(covid_api) # register api routes
app.register_blueprint(user_api) # register api routes
app.register_blueprint(game_api) # register api routes
app.register_blueprint(app_projects) # register app pages
app.register_blueprint(country_api)
app.register_blueprint(word_api)


@app.errorhandler(404)  # catch for URL not found
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/')  # connects default URL to index() function
def index():
    return render_template("index.html")

@app.route('/stub/')  # connects /stub/ URL to stub() function
def stub():
    return render_template("stub.html")

@app.route('/login/')  # connects /stub/ URL to stub() function
def login():
    return render_template("login.html")



@app.route('/games')
def games():
   # return render_template("games.html")
    url = "https://cvcepgames.duckdns.org/api/games/"

    response = requests.request("GET", url)

    output = response.json()
    return render_template("games.html",games=output)

@app.route('/jeopardy/')  # connects /stub/ URL to stub() function
def jeopardy():
    return render_template("jeopardy.html")


@app.before_first_request
def activate_job():
    initJokes()
    initUsers()
    initGames()
    initCountries()
    initWords()

# this runs the application on the development server
if __name__ == "__main__":
    # change name for testing
    from flask_cors import CORS
    cors = CORS(app)
    app.run(debug=True, host="0.0.0.0", port="8039")

    
