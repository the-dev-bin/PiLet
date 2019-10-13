import json
from operator import itemgetter
from typing import Dict, List

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

DATA = 'data.json'
app = Flask(__name__)

cors = CORS(app, resources={r"/foo": {"origins": "http://localhost:port"}})



@app.route("/getStatus", methods=['GET'])
@cross_origin(origin='localhost',headers=['Content-Type','Authorization'])
def get_status():
    return jsonify(get_next_pending())


@app.route("/postStatus", methods=['POST'])
@cross_origin(origin='localhost',headers=['Content-Type','Authorization'])
def post_status():
    print(request.get_data())
    return "recived"


@app.route("/scheduleEvent", methods=['POST'])
@cross_origin(origin='localhost',headers=['Content-Type','Authorization'])
def schedule():
    data = request.get_json()
    print(data)
    return jsonify(data)


@app.route("/getSchedule", methods=['GET'])
@cross_origin(origin='localhost',headers=['Content-Type','Authorization'])
def get_schedule():
    return jsonify(get_next_three_pending())


@app.route("/active", methods=['GET'])
@cross_origin(origin='localhost',headers=['Content-Type','Authorization'])
def is_active():
    return

@app.route('/test')
def testing():
    return "<form action='/' method='POST'><input type='submit'></form>"

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
    sorted_data = sorted(pending, key= itemgetter('start'))
    print(sorted_data)
    return sorted_data


def get_next_pending() -> Dict:
    data = filter_pending_data()
    return data[0]

def get_next_three_pending() -> List:
    data = filter_pending_data()
    print(data[0:3])
    return data[0:3]



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
