import datetime
import re
from typing import Dict

from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class API(Resource):

    def __inti__(self):
        pass

    # Returns a json file
    # returns next_start and length (A dictionary)
    def get_status(self):
        # Call get_data()
        # put contents of get_data() into json and return
        pass

    def get_data(self, file) -> Dict:
        # pulls data from json
        pass

    # Sends the json to the pi
    def post_status(self, file) -> None:
        pass

    @staticmethod
    def get_weather():
        pass


api.add_resouce(API, '/')

if __name__ == '__main__':
    app.run(debug=True)
