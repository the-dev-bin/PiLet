import json

from datetime import datetime, timezone
from dateutil.parser import parse 

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
    data = json.loads(request.get_json())
    start = data['start']
    status = data['status']
    print(start, " ", status)
    for event in get_data():
        if int(event['start']) == int(start):
            update_json(start, status)
    
    return "recived"


@app.route("/getData", methods=['GET'])
@cross_origin(origin='localhost',headers=['Content-Type','Authorization'])
def get_all():
    return jsonify(get_data())


@app.route("/scheduleEvent", methods=['POST'])
@cross_origin(origin='localhost',headers=['Content-Type','Authorization'])
def schedule():
    data = request.get_json()['data']
    date = data['date']
    time = data['time']

    #pull hours minutes from duration
    durration_time = data['duration']
    durration_time = durration_time[11:16] #hours and minutes between 11 and 16
    
    #pull timestamp from time and date
    start_time = date[:10] + time[10:] #date from date time from time

    #define start as epoch timestamp
    start = datetimetoepoch(start_time)
    end = start + stringtoseconds(durration_time)


    event = {
        "start" : int(start),
        "end" : int(end),
        "status" : "pending"
    }

    append_json(event)
    print(event)
    return jsonify(data)


@app.route("/getSchedule", methods=['GET'])
@cross_origin(origin='localhost',headers=['Content-Type','Authorization'])
def get_schedule():

    data = get_next_three_pending()
    for event in data:
        event['start'] = epochtodatetime(event['start'])
        event['end'] = epochtodatetime(event['end'])
    return jsonify(data)


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


def append_json(event):
    json_file =  open(DATA, 'r')
    data = json.load(json_file)
    json_file.close()

    data.append(event)

    json_file = open(DATA, 'w')
    json_file.write(json.dumps(data))
    json_file.close()

def update_json(start, status):
    json_file =  open(DATA, 'r')
    data = json.load(json_file)
    json_file.close()
    print(f"{start} {status}")
    for event in data:
        if event['start'] == start:
            print('updating')
            event['status'] = status

    json_file = open(DATA, 'w')
    json_file.write(json.dumps(data))
    json_file.close()


def datetimetoepoch(date_timestr)->int:
    date_object = parse(date_timestr)
    seconds = date_object.timestamp()
    return seconds


def stringtoseconds(time)->int:
    hours = int(time[:2])*60*60
    seconds = int(time[3:])*60
    return (hours+seconds)


def epochtodatetime(seconds)->str:
    dateobj = datetime.fromtimestamp(seconds, timezone.utc)
    return str(dateobj)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
