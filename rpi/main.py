import os
import time

from smarlet_request import get_content
from relay import get_state, gpio_off, gpio_on

PIN = 26


def main() -> None:


    data = get_content()

    start = int(data['start'])
    end = int(data['end'])

    if time.time() >= start and time.time() <= start + 300:
        if get_state(PIN) == 0:
            gpio_on(PIN)

    if time.time() >= end and time.time() <= end + 300:
        if get_state(PIN) == 1:
            gpio_off(PIN)


if __name__ == "__main__":
    main()
