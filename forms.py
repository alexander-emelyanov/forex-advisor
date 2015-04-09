from app import db, bcrypt
from models import User
from wtforms import form, fields, validators


# Define login and registration forms (for flask-login)
class LoginForm(form.Form):

    login = fields.StringField(validators=[validators.required()])
    password = fields.PasswordField(validators=[validators.required()])

    def validate_login(self, field):
        user = self.get_user()

        if user is None:
            raise validators.ValidationError('User not found')

        if not bcrypt.check_password_hash(user.passhash, self.password.data):
            raise validators.ValidationError('Invalid password')

    def get_user(self):
        return db.session.query(User).filter_by(username=self.login.data).first()