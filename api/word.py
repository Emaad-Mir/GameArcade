
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime

from model.words import Word

word_api = Blueprint('word_api', __name__,
                   url_prefix='/api/words')


# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(word_api)

class WordAPI:        
    class _Create(Resource):
        def post(self):
            ''' Read data for json body '''
            body = request.get_json()
            
            ''' Avoid garbage in, error checking '''
            # validate name
            word = body.get('word')
            if word is None or len(word) < 2:
                return {'message': f'Word is missing, or is less than 2 characters'}, 210



            ''' #1: Key code block, setup USER OBJECT '''
            wo = Word(word)
            
            ''' Additional garbage error checking '''
            # set password if provided
           
            
            ''' #2: Key Code block to add user to database '''
            # create user in database
            word_db = wo.create()
            # success returns json of user
            if word_db:
                return jsonify(word_db.read())
            else:
                return {'message': f'Processed {word_db}, either a format error or description {word} is duplicate'}, 210

    class _Read(Resource):
        def get(self):
            words = Word.query.all()    # read/extract all users from database
            json_ready = [word.read() for word in words]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps

    class _Delete(Resource):
        def delete(self, id):
            word = Word.query.get(id)
            if word:
                word.delete()
                return {'message': f'Game with ID {id} deleted'}, 200
            else:
                return {'message': f'Game with ID {id} not found'}, 404

    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')
    api.add_resource(_Delete, '/delete/<int:id>')
