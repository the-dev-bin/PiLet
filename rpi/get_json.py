import json

import requests

# URL = "hack.thedevbin.com:9000/getstatus"

# for testing
URL = "https://pastebin.com/raw/YrB02wei"


def get_content() -> json:
    content = requests.get(URL).content
    data = json.loads(content)
    return data


def main() -> None:
    get_content()


if __name__ == "__main__":
    main()
