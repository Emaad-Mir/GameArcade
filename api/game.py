
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime

from model.games import Game

from __init__ import app, db

game_api = Blueprint('game_api', __name__,
                   url_prefix='/api/games')


# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(game_api)

class GameAPI:        
    class _Create(Resource):
        def post(self):
            ''' Read data for json body '''
            print(request.is_json)
            body = request.get_json()
            print(body)
            print("lol")
            
            ''' Avoid garbage in, error checking '''
            # validate name
            name = body.get('name')
            if name is None or len(name) < 2:
                return {'message': f'Name is missing, or is less than 2 characters'}, 210
            # validate uid
            desc = body.get('desc')
            if desc is None or len(desc) < 2:
                return {'message': f'Description is missing, or is less than 2 characters'}, 210
            # look for password and dob
            date_made = body.get('date')
            link = body.get('link')
            if link is None or len(link) < 2:
                return {'message': f'Link is missing, or is less than 2 characters'}, 210


            ''' #1: Key code block, setup USER OBJECT '''
            go = Game(name, 
                      date_made, desc, link)
            
            ''' Additional garbage error checking '''
            # set password if provided
           
            if date_made is not None:
                try:
                    go.date = datetime.strptime(date_made, '%m-%d-%Y').date()
                except:
                    return {'message': f'Date made {date_made}, must be mm-dd-yyyy'}, 210
            
            ''' #2: Key Code block to add user to database '''
            # create user in database
            game = go.create()
            # success returns json of user
            if game:
                return jsonify(game.read())
            else:
                return {'message': f'Processed {name}, either a format error or description {desc} is duplicate'}, 210

    class _Read(Resource):
        def get(self):
            games = Game.query.all()    # read/extract all users from database
            json_ready = [game.read() for game in games]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps

    class _Delete(Resource):
        def delete(self, id):
            game = Game.query.get(id)
            if game:
                game.delete()
                return {'message': f'Game with ID {id} deleted'}, 200
            else:
                return {'message': f'Game with ID {id} not found'}, 404

    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')
    api.add_resource(_Delete, '/delete/<int:id>')
