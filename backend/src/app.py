# from api.test import test
from flask import Flask, render_template, request, jsonify, blueprints
from flask_restful import Api, Resource
from flask_cors import CORS

# from flask_cors import CORS
import json

# from redis import Redis
app = Flask(__name__)
CORS(app)
# app.register_blueprint(test, url_prefix='/api')

@app.route('/')
def hello():
    # redis.incr('hits')
    return "Hello"


@app.route("/hoge", methods=['GET'])
def getHoge():
    return jsonify({"lang": "Python"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
    # app.run(host="localhost", debug=True, port=8080)
