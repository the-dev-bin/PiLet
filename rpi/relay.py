#!/usr/bin/python3
import os
import time
import configparser
import RPi.GPIO as GPIO

config = configparser.ConfigParser()
config.read('../CONFIG.TXT')



def gpio_on(channel) -> None:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(channel, GPIO.OUT)
    state = 1
    try:
        GPIO.output(channel, state)
    except Exception:
        GPIO.output(channel, 0)
        GPIO.cleanup()


def gpio_off(channel) -> None:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(channel, GPIO.OUT)
    state = 0
    try:
        GPIO.output(channel, state)
    except Exception:
        GPIO.output(channel, 0)
        GPIO.cleanup()
        os.system('sudo reboot now')


def get_state(channel) -> GPIO:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(channel, GPIO.OUT)
    state = GPIO.input(channel)
    return state


def main() -> None:
    # read pin from config file
    PIN = config['RPI']['pin']
    gpio_on(PIN)
    time.sleep(5)
    gpio_off(PIN)


if __name__ == '__main__':
    main()
