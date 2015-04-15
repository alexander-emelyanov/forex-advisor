from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from sqlalchemy.exc import SQLAlchemyError
import os

from app import app
from models import *

app.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


@manager.command
def create_admin():
    print('Add admin user to the database. Use admin/QWErty13 credentials to login.')
    # Create default user
    user = User()
    user.username = 'admin'
    user.passhash = bcrypt.generate_password_hash('QWErty13')
    db.session.add(user)
    db.session.commit()


@manager.command
def cleardb():
    print('Each entity stored on DB will be removed...')
    try:
        # prepare removed models list
        removed_models = [Symbol, Market]

        for model in removed_models:  # remove each model entities
            num_rows_deleted = db.session.query(model).delete()
            print("{0} removed from table `{1}`".format(num_rows_deleted, model.__tablename__))

        # Final action...
        db.session.commit()

    except SQLAlchemyError as err:
        db.session.rollback()
        print("SQLAlchemy error occurred: {0}".format(err))

if __name__ == '__main__':
    manager.run()