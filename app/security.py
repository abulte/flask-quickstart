from flask.ext.security import Security, SQLAlchemyUserDatastore

from app import app, db
from app.models import User, Role

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
