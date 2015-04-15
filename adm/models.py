import flask_login as login
from flask_admin.contrib import sqla


# Create customized model view class
class UserModelView(sqla.ModelView):

    def on_model_change(self, form, model, is_created):
        if is_created:
            model.set_password(password=form.password.data)

    def is_accessible(self):
        return login.current_user.is_authenticated()


class SymbolModelView(sqla.ModelView):

    def is_accessible(self):
        return login.current_user.is_authenticated()


class MarketModelView(sqla.ModelView):

    def is_accessible(self):
        return login.current_user.is_authenticated()


class DirectionModelView(sqla.ModelView):

    def is_accessible(self):
        return login.current_user.is_authenticated()


class DurationModelView(sqla.ModelView):

    def is_accessible(self):
        return login.current_user.is_authenticated()


class PredictorModelView(sqla.ModelView):

    def is_accessible(self):
        return login.current_user.is_authenticated()


class SignalModelView(sqla.ModelView):

    def is_accessible(self):
        return login.current_user.is_authenticated()