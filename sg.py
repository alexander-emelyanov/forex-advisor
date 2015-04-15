import os
import datetime
from app import app, db
app.config.from_object(os.environ['APP_SETTINGS'])

from models import *
from sqlalchemy.exc import SQLAlchemyError


class SignalsGenerator:

    @staticmethod
    def run():

        signal = Signal()

        related_models = {'symbol_id': Symbol, 'duration_id': Duration, 'direction_id': Direction, 'predictor_id': Predictor}

        # Related models choosing
        for field,model in related_models.items():
            # print("Select * from {0}".format(model.__tablename__))
            model_instance = db.session.query(model).order_by(db.func.random()).first()
            # print("Extracted object: {0}".format(model_instance))
            setattr(signal, field, model_instance.id)

        # Time points generation
        signal.time_of_creation = datetime.datetime.utcnow()
        signal.opening_time = datetime.datetime.utcnow() + datetime.timedelta(seconds=60)
        signal.closing_time = datetime.datetime.utcnow() + datetime.timedelta(seconds=3660)

        try:
            db.session.add(signal)
            db.session.commit()
        except SQLAlchemyError as err:
            db.session.rollback()
            print("SQLAlchemy error occurred: {0}".format(err))

        return True


if __name__ == '__main__':
    SignalsGenerator.run()