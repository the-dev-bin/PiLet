import time
import RPi.GPIO as GPIO



def gpio_on(channel,seconds):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(channel, GPIO.OUT)
    start = int(time.time())
    state = 1
    try:
        GPIO.output(channel, state)
        time.sleep(seconds)
        state = 0
        GPIO.output(channel, state)
    except:
        GPIO.output(channel, 0)
        GPIO.cleanup()
        exit()

def main():
    gpio_on(37,30)




if __name__ == '__main__':
    main()   

