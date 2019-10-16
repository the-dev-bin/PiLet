import json

import requests

import configparser


config = configparser.ConfigParser()
config.read('../CONFIG.TXT')

# create urls from config file
getURL = config['api']['url'] + config['api']['port'] + '/getStatus'
postURL = config['api']['url'] + config['api']['port'] + '/postStatus'

def get_content() -> json:
    content = requests.get(getURL).content
    data = json.loads(content)
    return data


def send_status(status, start_time) -> None:
    data = {"status": status, "start": start_time}
    requests.post(postURL, json=json.dumps(data))


def main() -> None:
    get_content()


if __name__ == "__main__":
    main()
