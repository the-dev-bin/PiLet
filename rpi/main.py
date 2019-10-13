import os
import time

from smarlet_request import get_content, send_status
from relay import get_state, gpio_off, gpio_on

PIN = 26


def main() -> None:


    data = get_content()

    start = int(data['start'])
    end = int(data['end'])

    if time.time() >= start and time.time() <= start + 300:
        if get_state(PIN) == 0:
            gpio_on(PIN)
            send_status(start, 'pending')

    if time.time() >= end and time.time() <= end + 300:
        if get_state(PIN) == 1:
            gpio_off(PIN)
            send_status(start, 'done')



if __name__ == "__main__":
    main()
