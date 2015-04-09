import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

from models import *


@app.route('/')
def hello():
    return "Welcome to FOREX Advisor REST API"

if __name__ == '__main__':
    print("Used config object: {}".format(os.environ['APP_SETTINGS']))
    app.run()