import time, configparser

from relay import get_state, gpio_off, gpio_on
from smartlet_request import get_content, send_status


config = configparser.ConfigParser()
config.read('../CONFIG.TXT')

#read pin from config file
PIN = config['RPI']['pin']


def main() -> None:

    data = get_content()

    start = int(data['start'])
    end = int(data['end'])

    if time.time() >= start and time.time() <= start + 300:
        if get_state(PIN) == 0:
            gpio_on(PIN)
            send_status(start, 'active')

    if time.time() >= end and time.time() <= end + 300:
        if get_state(PIN) == 1:
            gpio_off(PIN)
            send_status(start, 'done')


if __name__ == "__main__":
    main()
