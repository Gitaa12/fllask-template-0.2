import json
import requests
import traceback
from flask import make_response, jsonify, current_app, request
from flask_restful import Resource, reqparse
from flask_sieve import Validator



class PokeDetail(Resource):
    @classmethod
   
    def get(cls, name):
        try:
            rules = {
                'name': ['required', 'alpha']
            }
            messages = {
                'name.required': 'Yikes! The name is required',
                'name.required': 'Yikes! The name is required'
                    
            }
            validator = Validator(rules=rules, messages=messages, request=request)
            if validator.passes():
                get_pokemon_name_url = f'https://pokeapi.co/api/v2/pokemon/{name}'
                r = requests.get(get_pokemon_name_url)
                return r.json()
            else:
                return make_response(jsonify(validator.error()),400)
        except Exception as e:
            current_app.logger.error(traceback.format_exc())
            return make_response(jsonify({'error':'internal server error'}),500)