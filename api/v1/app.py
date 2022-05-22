#!/usr/bin/python3


from flask import Flask
from models import storage
from flask import Flask
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)

@app.teardown_appcontext
def teardown_db(exception):
    storage.close()

if __name__ == "__main__":
    app.run(host= getenv('HBNB_API_HOST', '0.0.0.0'), port= getenv('HBNB_API_PORT', '5000'))
    threaded=True