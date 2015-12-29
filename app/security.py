from flask_jwt import JWT
from flask import jsonify

from app import app
from models import User

# TODO use my own route for login
# in order to be able to check for custom stuff
# like confirmed_at...


def authenticate(username, password):
    # TODO check user/pwd
    return User.query.first()


def identity(payload):
    user_id = payload['identity']
    return User.query.first()


def jwt_response_handler(access_token, user):
    resp_dict = {
        'id': user.id,
        'email': user.email,
        'access_token': access_token.decode('utf-8')
    }
    return jsonify(resp_dict)


jwt = JWT(app, authenticate, identity)
jwt.auth_response_handler(jwt_response_handler)
