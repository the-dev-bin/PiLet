from relay import gpio_on, get_state, gpio_off
from get_json import get_content
import time
import os

PIN = 26



def main():
    if time.time() > os.environ["START_TIME"] + (4 * 60 * 60):
        gpio_off(PIN)

    data = get_content()

    start = int(data['start'])
    end = int(data['end'])

    if time.time() >= start and time.time() <= start + 300:
        if get_state(PIN) == 0:
            os.environ["START_TIME"] = int(time.time())
            gpio_on(PIN)

    if time.time() >= end and time.time() <= end + 300:
        if get_state(PIN) == 1:
            gpio_off(PIN)


if __name__ == "__main__":
    main()