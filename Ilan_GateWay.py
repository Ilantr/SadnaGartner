from flask import Flask
from flask import json
from flask import Response
from flask import request
import os

class Server(object):
    """Server class"""
    app = Flask(__name__)

    @app.route("/", methods =['GET', 'POST'])
    def Welcome():
        return "Welcome to my page :)"

    if __name__ == '__main__':
        app.debug = True
        port = int(os.environ.get('PORT', 5000))
        app.run(host = '0.0.0.0', port = port)