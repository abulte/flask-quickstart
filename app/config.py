# -*- coding: utf-8 -*-

import os

ENV = os.environ.get('ENVIRONMENT', 'dev')
SECRET_KEY = os.environ.get('SECRET_KEY', '(R)ze§§adm12313lkmjazML3z')
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECURITY_PASSWORD_HASH = 'bcrypt'
SECURITY_PASSWORD_SALT = SECRET_KEY
# -> /confirm
SECURITY_CONFIRMABLE = False
# -> /register
SECURITY_REGISTERABLE = True
# -> /reset
SECURITY_RECOVERABLE = False
# -> /change
SECURITY_CHANGEABLE = True
SECURITY_TRACKABLE = False
SECURITY_PASSWORDLESS = False

CSRF_ENABLED = True

MAIL_SERVER = os.environ.get('MAIL_SERVER', 'localhost')
MAIL_PORT = os.environ.get('MAIL_PORT', 25)
MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', False)
MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL', False)
MAIL_USERNAME = os.environ.get('MAIL_USERNAME', None)
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', None)
MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER', None)

if ENV == 'dev':
    # set to False to send email on dev
    MAIL_SUPPRESS_SEND = True
    DEBUG = True
else:
    DEBUG = False
