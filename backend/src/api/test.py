from flask import Flask, render_template, request, jsonify, Blueprint
from flask_restful import Api, Resource
from flask_cors import CORS

app1 = Blueprint('app1', _name_,)


@app1.route('/test')
def test():
    return jsonify({"test": "test"})
