#!/usr/bin/python3
""" states file"""
from flask import jsonify
from api.v1.views import app_views
from models import storage

@app_views.route('/states', strict_slashes=False)
def get_to_dict():
    """ to retrieve an object into a valid JSON"""
    result = []
    state_list = storage.all('State')
    for i in state_list.values():
        result.append(i.to_dict())
    return jsonify(result)
