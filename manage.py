# -*- coding: utf-8 -*-
from datetime import datetime
from flask.ext.script import Manager, Server
from flask_failsafe import failsafe
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.security.registerable import register_user

from app import app, db
from app.security import user_datastore
from app.models import User


@failsafe
def create_app():
    from app import app
    return app

manager = Manager(create_app)
manager.add_command('runserver', Server())
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def create_superuser(email, password):
    admin = user_datastore.find_or_create_role('admin')

    user = User.query.filter_by(email=email).first()
    if not user:
        user = register_user(email=email, password=password)
        user.confirmed_at = datetime.now()
        db.session.add(user)
        db.session.commit()

    user_datastore.add_role_to_user(user, admin)
    db.session.commit()

if __name__ == "__main__":
    manager.run()
