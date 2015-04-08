from flask import Flask
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])


@app.route('/')
def hello():
    return "Welcome to FOREX Advisor REST API"

if __name__ == '__main__':
    print("Used config object: {}".format(os.environ['APP_SETTINGS']))
    app.run()