# -*- coding: utf-8 -*-

from flask_jwt import jwt_required
from flask.ext.restful import Resource
from flask.ext.restful import abort
from flask import request


class BaseResource(Resource):

    def _get_attrs(self, attrs):
        attrs_dict = {}
        for attr in attrs:
            if attr in request.form:
                attrs_dict[attr] = request.form[attr]
            elif request.json and attr in request.json:
                attrs_dict[attr] = request.json[attr]
        return attrs_dict

    def _validate_attrs(self, attrs):
        attrs_dict = {}
        for attr in attrs:
            if attr not in request.form and (not request.json or attr not in request.json):
                abort(400, description='Missing attr %s' % attr)
            else:
                attrs_dict[attr] = request.form[attr] if attr in request.form else request.json[attr]
        return attrs_dict

    def _validate_attr(self, attr):
        if attr not in request.form and attr not in request.json:
            abort(400, description='Missing attr %s' % attr)
        return request.form[attr] if attr in request.form else request.json[attr]


# TODO not working, decorator not compliant
class ProtectedResource(BaseResource):
    method_decorators = [jwt_required, ]
    # pass
