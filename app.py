import os
from flask import Flask, session, request, flash, url_for, redirect, render_template, abort ,g
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from forms import *
from models import *

# Flask admin packages
import flask_admin as admin
from flask_admin import helpers, expose
from adm.models import *


# Initialize flask-login
def init_login():
    login_manager = login.LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'signin'

    # Create user loader function
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(User).get(user_id)


# Create customized index view class that handles login & registration
class AdminIndexView(admin.AdminIndexView):

    @expose('/')
    def index(self):
        if not login.current_user.is_authenticated():
            return redirect(url_for('.login_view'))
        return super(AdminIndexView, self).index()

    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):

        login_form = LoginForm(request.form)
        if helpers.validate_form_on_submit(login_form):
            user = login_form.get_user()
            login.login_user(user)

        if login.current_user.is_authenticated():
            return redirect(url_for('.index'))
        self._template_args['form'] = login_form
        return super(AdminIndexView, self).index()

    @expose('/logout/')
    def logout_view(self):
        login.logout_user()
        return redirect(url_for('.index'))


# Routes section


@app.route('/')
def index():
    return render_template('index.html')


# Initialize flask-login
init_login()

# Create admin
admin = admin.Admin(app, 'Forex Advisor: Control Panel', index_view=AdminIndexView(), base_template='my_master.html', template_mode='bootstrap3')

# Add view
admin.add_view(UserModelView(User, db.session))
admin.add_view(SymbolModelView(Symbol, db.session))
admin.add_view(MarketModelView(Market, db.session))

# Import ModelViews for Flask-Admin
admin.add_view(DirectionModelView(Direction, db.session))
admin.add_view(DurationModelView(Duration, db.session))
admin.add_view(PredictorModelView(Predictor, db.session))
admin.add_view(SignalModelView(Signal, db.session))


if __name__ == '__main__':
    print("Used config object: {}".format(os.environ['APP_SETTINGS']))
    app.run()