import time

import RPi.GPIO as GPIO


def relay_setup(channel) -> None:
    GPIO.setboard(GPIO.BOARD)
    GPIO.setup(channel, GPIO.OUT)

    for i in range(50):
        GPIO.output(channel, True)
        time.sleep(1)
        print('On')
        GPIO.output(channel, False)
        time.sleep(1)
        print('Off')

    GPIO.cleanup()
