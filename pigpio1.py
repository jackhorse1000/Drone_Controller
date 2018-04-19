import time
import signal
import sys
import pigpio


#Set GPIO pin numbering


#Access the Rpi
pi = pigpio.pi()
print(pi.connected)

pi.set_mode(36, pigpio.OUTPUT)


while(1):
    pi.set_servo_pulsewidth(36, 1500) #Maximum

