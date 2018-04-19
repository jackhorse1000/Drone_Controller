import RaspColorSensor
# import sensors as rightSensor
# import sensors2 as frontSensor
# import sensors3 as leftSensor
# import sensors4 as backSensor
import sensors5 as heightSensor
import hella_PWNs as startup
import changeDc as change

from enum import Enum

class State(Enum):
    START = 0
    MOVETOMIDDLE = 1
    MOVETOROOM = 2
    SEARCHING = 3
    FOUND = 4
    MOVETOLAND = 5
    LAND = 6


state = State.START

hoverspeed = 7
errorRange = 5

distanceAllowance = 10
heightAllowance = 5

currentSpeed = 7.75

frontDist = 0
leftDist = 0
rightDist = 0
backDist = 0
currentHeight = 0

targetHeight = 102
atTargetHeight = False

def mean(distances):
    distances.sort()
    sum = 0
    i=0
    for distance in distances:
        if(distance > distances[(len(distances)-1)//2] + 20):
            distances.remove(distance)
        else:
            i = i+1
            sum += distance
    return sum/float(i)

def diffInTargetHeight(currentHeight):
    if(currentHeight >= targetHeight+heightAllowance):
        #do something to lower it
        change.slowDown(currentSpeed)
    elif(currentHeight <= targetHeight-heightAllowance):
        change.speedUp(currentSpeed)


#
#
#
def updateDistances():
    heightDistances = []
    for i in range(errorRange):
        heightDistances.append(heightSensor.getDistance())
    currentHeight = mean(heightDistances)
    print(currentHeight)

# frontDistances = []
#     rightDistances = []
#     leftDistances = []
#     backDistances = []

#     #front sensor distance
#     for i in range(errorRange):
#         frontDistances.append(frontSensor.getDistance())
#     self.frontDist = mean(frontDistances)
#     print(self.frontDist)
#
#     #right sensor distance
#     for i in range(errorRange):
#         rightDistances.append(rightSensor.getDistance())
#     self.rightDist = mean(rightDistances)
#     print(self.rightDist)
#
#     #left sensor distance
#     for i in range(errorRange):
#         leftDistances.append(leftSensor.getDistance())
#     self.leftDist = mean(leftDistances)
#     print(self.leftDist)
#
#     #back sensor distance
#     for i in range(errorRange):
#         backDistances.append(backSensor.getDistance())
#     self.backDist = mean(backDistances)
#     print(self.backDist)

def calcDiff(actual,target):
    return target-actual
#
# #check the the distances fall the given range for moving to the middle
def movedToMiddle():
    frontTarget = 120
    backTarget = 143
    rightTarget = 65

    if((frontDist-frontTarget)**2<=distanceAllowance**2):

        if ((backDist - backTarget) ** 2 <= distanceAllowance ** 2):

            if ((rightDist - rightTarget) ** 2 <= distanceAllowance ** 2):
                return True
    else: #calculate the difference and give to controller
        if ((backDist - backTarget) ** 2 >= distanceAllowance ** 2):
            backDiff = calcDiff(backDist,backTarget)
            if(backDiff>0):
                change.goBack(hoverspeed)
            if (backDiff < 0):
                change.goForward(hoverspeed)
        if ((rightDist - rightTarget) ** 2 >= distanceAllowance ** 2):
            rightDiff = calcDiff(rightDist, rightTarget)
            if (rightDiff > 0):
                change.rollRight(hoverspeed)
            if(rightDiff<0):
                change.rollLeft(hoverspeed)

def movedToRoom():
    frontTarget = 130
    rightTarget = 95
    leftTarget = 115

    if ((frontDist - frontTarget) ** 2 <= distanceAllowance ** 2):

        if ((leftDist - leftTarget) ** 2 <= distanceAllowance ** 2):

            if ((rightDist - rightTarget) ** 2 <= distanceAllowance ** 2):
                return True
    else:  # calculate the difference and give to controller
        if ((frontDist - frontTarget) ** 2 >= distanceAllowance ** 2):
            frontDiff = calcDiff(frontDist, frontTarget)
            if(frontDiff>0):
                change.goForward(hoverspeed)
            if(frontDiff<0):
                change.goBack(hoverspeed)
        if ((rightDist - rightTarget) ** 2 >= distanceAllowance ** 2):
            rightDiff = calcDiff(rightDist, rightTarget)
            if(rightDiff>0):
                change.rollRight()
            if(rightDiff<0):
                change.rollLeft()


#while in start camera detects red or not green
while state == State.START:
    updateDistances()
    #check cameras for color change and update color sensor readings
    if RaspColorSensor.seeGreen():
        state = State.MOVETOMIDDLE
        print('GREEN!')
        startup.init()
        startup.armThatShit()
        startup.pedalToTheMetal()
        diffInTargetHeight(currentHeight)

#
# #move to the middle of the first tent
while state == State.MOVETOMIDDLE:
    updateDistances()
    diffInTargetHeight(currentHeight)
    if(movedToMiddle()):
        state = State.MOVETOROOM
# #
# # #move to the second tent
# while state == State.MOVETOROOM:
#     updateDistances()
#     diffInTargetHeight(currentHeight)
#     if(movedToRoom()):
#         state = State.SEARCHING
# #
# #
# # #start searching for faulty generator
# while state == State.SEARCHING:
#     updateDistances()
#     diffInTargetHeight(currentHeight)
#     movedToRoom()
#     if(RaspColorSensor.lookForRed()):
#         state = State.MOVETOLAND
#
# while state == State.MOVETOLAND:
#      updateDistances()
#      if(movedToLand()):
#
#
#
# #We are taking off and have seen green
# #raises till it is the target height
# while start:
#     #maybe wait a second so the sensor doesn't mess up
#     updateDistances()
#
# #raise the prob here until we get decent height readings
#
#
# #change mode to mission and guide into generator room
#
#
# # spin drone to view all the motors and use camera
# # to sense red and take a photo
# while searching:
#     seenGenerator = RaspColorSensor.lookForRed()
#     if(seenGenerator):
#         searching = False
#
#
#
#
# #we have a photo of the bad generator
# #return to take-off and landing point
#
# #maybe return to guide mode and land the probe and turn off propellers
#
# #transmit the image
#
#
#
#
