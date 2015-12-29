# -*- coding: utf-8 -*-
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask.ext.cors import CORS

from app import config

app = Flask(__name__)
app.config.from_object(config)

Mail(app)
CORS(app)
db = SQLAlchemy(app)

from app import views  # NOQA
from app import models
from app import api
from app import security
