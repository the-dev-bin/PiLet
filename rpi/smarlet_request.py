import json

import requests

getURL = "http://hack.thedevbin.com:9000/getStatus"
postURL = "http://hack.thedevbin.com:9000/postStatus"

# for testing
#URL = "https://pastebin.com/raw/YrB02wei"


def get_content() -> json:
    content = requests.get(getURL).content
    data = json.loads(content)
    return data


def send_status(status, start_time) -> None:
    data = '[{"status":' + status  + ', "start": ' + str(start_time) + '}]'
    requests.post(postURL, data=(data))


def main() -> None:
    get_content()


if __name__ == "__main__":
    main()
