# -*- coding: utf-8 -*-

import bcrypt
from datetime import datetime
from flask_restful import Api
from flask_restful import marshal_with
from flask_restful import abort

from flask_jwt import jwt_required

import serializers
from .security import jwt
from app import app, db
from app.models import User
from .base import BaseResource

api = Api(app, prefix='/api')


class Users(BaseResource):

    @marshal_with(serializers.user)
    @jwt_required()
    def get(self):
        users = User.query.all()
        return users


class Signup(BaseResource):

    @marshal_with(serializers.user_w_token)
    def post(self):
        attrs = ['email', 'password']
        attrs = self._validate_attrs(attrs)
        existing = User.query.filter_by(email=attrs['email']).first()
        if existing:
            abort(400, description='Email already used.')
        hashed = bcrypt.hashpw(attrs['password'].encode('utf-8'), bcrypt.gensalt())
        user = User(email=attrs['email'], password=hashed, created_at=datetime.now())
        db.session.add(user)
        db.session.commit()
        user.access_token = jwt.jwt_encode_callback(user)
        return user


class Login(BaseResource):

    @marshal_with(serializers.user_w_token)
    def post(self):
        attrs = ['email', 'password']
        attrs = self._validate_attrs(attrs)

        user = User.query.filter_by(email=attrs['email']).first()
        if not user:
            return abort(401, description='Wrong credentials')

        hashed = bcrypt.hashpw(attrs['password'].encode('utf-8'), user.password.encode('utf-8'))
        if hashed != user.password:
            return abort(401, description='Wrong credentials')

        user.access_token = jwt.jwt_encode_callback(user)
        return user


api.add_resource(Users, '/users')
api.add_resource(Signup, '/signup')
api.add_resource(Login, '/login')
