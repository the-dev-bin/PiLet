import time
import RPi.GPIO as GPIO



def gpio_on(channel,seconds):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(channel, GPIO.OUT)
    start = int(time.time())
    print("turning on")
    state = 1
    try:
        GPIO.output(channel, state)
        time.sleep(seconds)
        print("turning off")
        state = 0
        GPIO.output(channel, state)
    except exception as e:
        GPIO.output(channel, 0)
        GPIO.cleanup()
        exit()

def main():
    gpio_on(26,10)




if __name__ == '__main__':
    main()   

