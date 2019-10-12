from typing import Tuple

import RPi.GPIO as GPIO


def relay_setup(channel_list: Tuple) -> None:
    GPIO.setboard(GPIO.BOARD)
    GPIO.setup(channel_list[0], GPIO.IN)
    GPIO.setup(channel_list[1], GPIO.OUT)
    GPIO.setup(channel_list[2], GPIO.OUT, initial=GPIO.HIGH)
