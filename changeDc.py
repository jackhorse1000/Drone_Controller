import RPi.GPIO as gpio
import time
import hella_PWNs

def goBack(hoverSpeed):
     hella_PWNs.pitchChangeDC(5.5)
     hella_PWNs.throttleChangeDC(hoverSpeed+1)

def goForward(hoverSpeed):
     hella_PWNs.pitchChangeDC(8.5)
     hella_PWNs.throttleChangeDC(hoverSpeed+1) #add value

def stopMoving(hoverSpeed):
    hella_PWNs.pitchChangeDC(7)
    hella_PWNs.throttleChangeDC(hoverSpeed)

def rollLeft(hoverspeed):
    hella_PWNs.rollChangeDC(7.75)
    hella_PWNs.throttleChangeDC(hoverspeed)

def rollRight(hoverspeed):
    hella_PWNs.rollChangeDC(6.25)
    hella_PWNs.throttleChangeDC(hoverspeed)

def speedUp(currentSpeed):
    hella_PWNs.throttleChangeDC(currentSpeed+ 0.5)

def slowDown(currentSpeed):
    hella_PWNs.throttleChangeDC(currentSpeed-0.5)
