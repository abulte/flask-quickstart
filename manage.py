# -*- coding: utf-8 -*-
from datetime import datetime
from flask.ext.script import Manager, Server
from flask_failsafe import failsafe
from flask.ext.migrate import Migrate, MigrateCommand

from app import app, db
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
    user = User.query.filter_by(email=email).first()
    if not user:
        user = User(email=email, password=password)
        user.confirmed_at = datetime.now()
        db.session.add(user)
        db.session.commit()

if __name__ == "__main__":
    manager.run()
