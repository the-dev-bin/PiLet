import json
from typing import Dict, List

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

DATA = 'data.json'
app = Flask(__name__)

cors = CORS(app, resources={r"/foo": {"origins": "http://localhost:port"}})

@app.route("/status", methods=['GET', 'POST'])
@cross_origin(origin='localhost',headers=['Content-Type','Authorization'])
def status():
    if (request.method == 'POST'):
        info = request.get_json()
        return jsonify({'info': info}), 201
    else:
        return json.dumps(get_next_pending())


def get_data() -> List:
    with open(DATA) as json_file:
        data = json.load(json_file)
    return data


def filter_pending_data() -> List:
    data = get_data()
    pending = []
    for event in data:
        if event['status'] == 'pending':
            pending.append(event)
        else:
            continue
    return pending


def get_next_pending() -> Dict:
    data = filter_pending_data()
    current = data[0]
    print(current)
    for event in data:
        print(event['start'])
        if int(event['start']) < int(current['start']):
            current = event
    return current


@app.route('/test')
def testing():
    return "<form action='/' method='POST'><input type='submit'></form>"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
