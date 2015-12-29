# -*- coding: utf-8 -*-
from flask_restful import Resource, Api
from flask_restful import marshal_with

from app import app
from app.models import User
import serializers

api = Api(app, prefix='/api')


class Users(Resource):

    @marshal_with(serializers.user)
    def get(self):
        users = User.query.all()
        return users


class Login(Resource):

    @marshal_with(serializers.user)
    def post(self):
        return {}


api.add_resource(Users, '/users')
api.add_resource(Login, '/login')
