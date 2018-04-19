import RPi.GPIO as GPIO
import time
import signal
import sys
import io

#Set GPIO pin numbering
GPIO.setmode(GPIO.BCM)

#Ouput sensor GPIO 13 [Pin 33]
TRIG = 13

#Input sensor GPIO 19 [pin 35]
ECHO = 19

def close(signals, frame):
    print("Turning off sensor")
    GPIO.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, close)


GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

def getDistance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    startTime = time.time()
    stopTime = time.time()

    while 0 == GPIO.input(ECHO):
        startTime = time.time()

    while 1 == GPIO.input(ECHO):
        stopTime = time.time()

    timeElapsed = stopTime - startTime
    distance = (timeElapsed * 34300)/2
    time.sleep(0.1)
    return distance