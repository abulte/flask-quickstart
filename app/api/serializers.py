# -*- coding: utf-8 -*-

import time
from flask_restful import fields


class JSTimestamp(fields.Raw):

    def format(self, value):
        if value is not None:
            return time.mktime(value.timetuple()) * 1000


user = {
    'id': fields.Integer,
    'first': fields.String,
    'last': fields.String,
    'email': fields.String,
    'confirmed_at': JSTimestamp
}

user_w_token = user.copy()
user_w_token.update({
    'access_token': fields.String
})
