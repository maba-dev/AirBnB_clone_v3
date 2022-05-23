#!/usr/bin/python3

""" my api"""

from flask import Flask
from models import storage
from flask import Flask
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)
@app.teardown_appcontext
def teardown_db(exception):
    """ app teardown"""
    storage.close()


if __name__ == "__main__":
    app.run(
        host=getenv('HBNB_API_HOST'), port=getenv('HBNB_API_PORT'),
        threaded=True
        )
