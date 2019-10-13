import requests 
import json

# URL = "hack.thedevbin.com:9000/getstatus"

# for testing
URL = "https://pastebin.com/raw/YrB02wei"


def get_content():
    content = requests.get(URL).content
    data = json.loads(content)
    return data

def send_status(status, start_time):
    data = { "status" : status, "start" : start_time}

    requests.post(URL,json=json.dumps(data))

def main():
    get_content()

if __name__ == "__main__":
    main()