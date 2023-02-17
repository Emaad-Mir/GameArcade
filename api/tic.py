from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime

from model.tics import Tic

from __init__ import app, db

tic_api = Blueprint('tic_api', __name__,
                   url_prefix='/api/tics')


# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(tic_api)

class ticAPI:        
    class _Create(Resource):
        def post(self):
            ''' Read data for json body '''
            print(request.is_json)
            body = request.get_json()
            name = body.get('name')
            score = body.get('score')
            
            ''' Avoid garbage in, error checking '''
            # validate name
            name = body.get('name')
            if name is None or len(name) < 2:
                return {'message': f'Name is missing, or is less than 2 characters'}, 210
            if score is None or score <=0:
                return {'message': f'Score is missing, or is less than 0'}, 210

            tic = Tic(name=name, score=score)
            user = tic.create()

            if user:
                return jsonify(user.read())
            return {'message': f'either your name or score are invalid'}


    class _Read(Resource):
        def get(self):
            tics = Tic.query.all()    # read/extract all users from database
            json_ready = [tic.read() for tic in tics]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps

    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')