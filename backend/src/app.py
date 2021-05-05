from flask import Flask, render_template, request, jsonify
# from redis import Redis


app = Flask(__name__)
# redis = Redis(host='redis', port=6379)

# @app.route('/')
# def hello():
#     redis.incr('hits')
#     return "Hello"


@app.route('/')
def Hello():
    return "Hello"



@app.route('/route')
def route():
    return "route"


@app.route("/hoge", methods=['GET'])
def getHoge():
    return jsonify({"lang": "Python"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
