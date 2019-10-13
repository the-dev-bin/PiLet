import json
from typing import Dict

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def status():
    if (request.method == 'POST'):
        info = request.get_json()
        return jsonify({'info': info}), 201
    else:
        return jsonify({"about": "Hello World"})


# Pulls data from a json file
def get_data(file) -> Dict:
    pass


@app.route('/test')
def testing():
    return "<form action='/' method='POST'><input type='submit'></form>"


if __name__ == "__main__":
    app.run(debug=True)
