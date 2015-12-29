# -*- coding: utf-8 -*-
from flask_restful import fields

user = {
    'id': fields.Integer,
    'first': fields.String,
    'last': fields.String,
    'email': fields.String
}
