#!/usr/bin/python3
import time
import RPi.GPIO as GPIO
import os

def gpio_on(channel):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(channel, GPIO.OUT)
    state = 1
    try: 
        GPIO.output(channel, state)
    except:
        GPIO.output(channel, 0)
        GPIO.cleanup()

def gpio_off(channel):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(channel, GPIO.OUT)
    state = 0
    try: 
        GPIO.output(channel, state)
    except:
        GPIO.output(channel, 0)
        GPIO.cleanup()
        os.system('sudo reboot now')


def get_state(channel):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(channel, GPIO.OUT)
    state = GPIO.input(channel)
    return state


def main():
    gpio_on(PIN)
    time.sleep(5)
    gpio_off(PIN)




if __name__ == '__main__':
    main()   

