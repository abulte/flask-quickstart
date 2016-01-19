# -*- coding: utf-8 -*-

import sys
import logging
from flask_jwt import JWT, logger as jwt_logger

from app import app

# fix flask_jwt faulty logging
loghandler = logging.StreamHandler(stream=sys.stdout)
jwt_logger.addHandler(loghandler)

jwt = JWT(app)
