from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime

from model.countries import Countries

country_api = Blueprint('country_api', __name__,
                   url_prefix='/api/countries')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(country_api)

class CountryAPI:    
    class _Create(Resource):
        def post(self):
            ''' Read data for json body '''
            body = request.get_json()
            
            ''' Avoid garbage in, error checking '''
            # validate name
            name = body.get("name")
            if name is None or len(name) < 2:
                return {'message': f'Name is missing, or is less than 2 characters'}, 210
            # validate uid
            cid = body.get('cid')
            #if cid is None or len(cid) < 2:
             #   return {'message': f'User ID is missing, or is less than 2 characters'}, 210
            # look for password and dob
            #password = body.get('password')
            #dob = body.get('dob')

            ''' #1: Key code block, setup USER OBJECT '''
            uo = Countries(name)
            
            ''' Additional garbage error checking '''
            # set password if provided
            #if password is not None:
             #   uo.set_password(password)
            # convert to date type
            #if dob is not None:
             #   try:
              #      uo.dob = datetime.strptime(dob, '%m-%d-%Y').date()
               # except:
                # return {'message': f'Date of birth format error {dob}, must be mm-dd-yyyy'}, 210
            
            ''' #2: Key Code block to add user to database '''
            # create user in database
            user = uo.create()
            # success returns json of user
            if user:
                return jsonify(user.read())
            # failure returns error
            return {'message': f'Processed {name}, either a format error or User ID {cid} is duplicate'}, 210

    class _Read(Resource):
        def get(self):
            countries = Countries.query.all()    # read/extract all users from database
            json_ready = [country.read() for country in countries]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps
    
    class _Update(Resource):
        def put(self):
            countries = Countries.query.all()    # read/extract all users from database
            json_ready = [country.read() for country in countries]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps
    '''
    class _Delete(Resource):
        def delete(self,id=None):
            newcountry = Countries.query.get(id)    # read/extract all users from database
            if newcountry:
                #newcountry.delete(self,id)
                return {"sucessfully deleted":f"{id}"}, 200
            else:
                return {"item not found":f"{id}"}, 404
            """_summary_

            Returns:
                _type_: _description_
            """    
    '''
    class _Delete(Resource):
        def delete(self, id):
            if id == 1000:
                countries1 = Countries.query.all()
                json_ready = [country.delete() for country in countries1]
                return jsonify(json_ready)
            else:
                newcountry = Countries.query.get(id)    # read/extract all users from database
                newcountry.delete()
                return {'message': f'successfully deleted {id}'}
            

        
            
    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')
    api.add_resource(_Update, '/update')
    api.add_resource(_Delete, '/delete/<int:id>')