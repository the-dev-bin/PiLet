import time
import RPi.GPIO as GPIO



def gpio_on(channel,seconds):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(channel, GPIO.OUT)
    start = int(time.time())
    state = 1
    GPIO.output(channel, state)
    while True:
        time.sleep(5)
        if(int(time.time()) >= (start + seconds)):
            state = 0
            break
    GPIO.output(channel, state)


def main():
    gpio_on(37,30)




if __name__ == '__main__':
    main()   