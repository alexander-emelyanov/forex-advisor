from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
import os

from app import app, db, bcrypt
from models import User

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

if __name__ == '__main__':
    manager.run()