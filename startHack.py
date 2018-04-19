import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(32, gpio.OUT)
pwm = gpio.PWM(32, 50)
pwm.start(7.5) #Good range between 4.5 - 10.5
time.sleep(10)
pwm.stop()
gpio.cleanup()
