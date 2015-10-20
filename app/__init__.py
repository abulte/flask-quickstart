# -*- coding: utf-8 -*-
from flask import Flask
from flask_bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask_mail import Mail

from app import config

app = Flask(__name__)
app.config.from_object(config)

Mail(app)
Bootstrap(app)
db = SQLAlchemy(app)

from app import views  # NOQA
from app import models
from app import security
from app import admin
