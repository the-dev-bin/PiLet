import json

import requests

URL = "http://hack.thedevbin.com:9000/getStatus"

# for testing
#URL = "https://pastebin.com/raw/YrB02wei"


def get_content() -> json:
    content = requests.get(URL).content
    data = json.loads(content)
    return data


def send_status(status, start_time) -> None:
    data = {"status": status, "start": start_time}
    requests.post(URL, json=json.dumps(data))


def main() -> None:
    get_content()


if __name__ == "__main__":
    main()
