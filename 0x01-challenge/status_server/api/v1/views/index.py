#!/usr/bin/python3
"""
The Index view
"""
from flask import jsonify

from api.v1.views import app_views


@app_views.route('/api/v1/status', methods=['GET'], strict_slashes=False)
def status():
    """
    The Status of the web server
    """
    return jsonify({"status": "OK"})
