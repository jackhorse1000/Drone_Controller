import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

# Given pins

freq_pwm = 50
arm_pin = 12
throttle_pin = 16
pitch_pin = 26
roll_pin = 20
yaw_pin = 21

# Setting up the pins

# Arm pin 
gpio.setup(arm_pin, gpio.OUT)
pwmArm = gpio.PWM(arm_pin, freq_pwm)

# Throttle pin 
gpio.setup(throttle_pin,gpio.OUT)
pwmThrottle = gpio.PWM(throttle_pin, freq_pwm)

# Pitch pin
gpio.setup(pitch_pin, gpio.OUT)
pwmPitch = gpio.PWM(pitch_pin,freq_pwm)

# Roll pin
gpio.setup(roll_pin,gpio.OUT)
pwmRoll = gpio.PWM(roll_pin, freq_pwm)

# Yaw pin
gpio.setup(yaw_pin,gpio.OUT)
pwmYaw = gpio.PWM(yaw_pin, freq_pwm)

# Init for Arm
def Arm():    
    pwmArm.start(4.5) # Good range between 4.5 - 10.5    
    print("Arm success")

# Change duty cycle for ARM
def armChangeDC(dutyCycle):
    pwmArm.ChangeDutyCycle(dutyCycle)

# Init for Throttle
def Throttle():    
    pwmThrottle.start(4.5)   
    print("Throttle success")

# Change duty cycle for throttle
def throttleChangeDC(dutyCycle):
    pwmThrottle.ChangeDutyCycle(dutyCycle)

# Init for pitch
def Pitch():    
    pwmPitch.start(7.15)
    print("Pitch success")

# Change duty cycle for pitch
def pitchChangeDC(dutyCycle):
    pwmPitch.ChangeDutyCycle(dutyCycle)

# Init for roll
def Roll():    
    pwmRoll.start(7.15)
    print("Roll success")

# Change duty cycle for roll
def rollChangeDC(dutyCycle):
    pwmRoll.ChangeDutyCycle(dutyCycle)

# Init for yaw
def Yaw():
    pwmYaw.start(7.15)
    print("Yaw success")

# Change duty cycle for yaw
def yawChangeDC(dutyCycle):
    pwmYaw.ChangeDutyCycle(dutyCycle)

# end GPIO
# def endGPIO():
#     pwmYaw.stop()
#     pwmRoll.stop()
#     pwmPitch.stop()
#     pwmThrottle.stop()
#     pwmArm.stop()
#     gpio.cleanup()

# Initialise all pins   
def init():
    Arm()
    Throttle()
    Pitch()
    Yaw()
    Roll()
    time.sleep(10)

def armThatShit():
    pwmArm.ChangeDutyCycle(10.5)
    time.sleep(5)

def pedalToTheMetal():
    pwmThrottle.ChangeDutyCycle(7.5)
    time.sleep(3)

# def decreaseYaw():
#     pwmYaw.ChangeDutyCycle(5)
#     time.sleep(5)

# # Essentially main call
# init()
# armThatShit()
# pedalToTheMetal()
# #decreaseYaw()
# gpio.cleanup()
