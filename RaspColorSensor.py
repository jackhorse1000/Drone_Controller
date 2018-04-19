from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np
import time
import cv2
from time import sleep

# # set up raspberry pi camera
# camera = PiCamera()
# camera.resolution = (640, 480)
# camera.framerate = 32
# rawCapture = PiRGBArray(camera, size=(640, 480))
#
# # allow the camera to warmup
# time.sleep(0.1)

def seeGreen():
    # set up raspberry pi camera
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 32
    rawCapture = PiRGBArray(camera, size=(640, 480))

    # allow the camera to warmup
    time.sleep(0.1)

    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

        # convert to hsv
        img_frame = frame.array
        hsv = cv2.cvtColor(img_frame, cv2.COLOR_BGR2HSV)

        lower_red = np.array([0, 100, 100])
        upper_red = np.array([10, 255, 255])
        lower_red2 = np.array([160, 100, 100])
        upper_red2 = np.array([179, 255, 255])

        mask_red_min = cv2.inRange(hsv, lower_red, upper_red)
        mask_red_max = cv2.inRange(hsv, lower_red2, upper_red2)
        red_hue_image = cv2.addWeighted(mask_red_min, 1.0, mask_red_max, 1.0, 0.0)

        sensitivity_green = 15;
        lower_green = np.array([60 - sensitivity_green, 100, 50])
        upper_green = np.array([60 + sensitivity_green, 255, 255])

        mask_green = cv2.inRange(hsv, lower_green, upper_green)

        if(cv2.countNonZero(mask_green)>cv2.countNonZero(red_hue_image)):
            return True

        # need to refresh buffer
        rawCapture.truncate(0)
    
    return False


percentageOfColorForPhoto = 0.17

def isRedColor(image, threshold):
    ratio = cv2.countNonZero(image)/float(640*480)
    print(cv2.countNonZero(image)/float(640*480))
    return ratio>=threshold


def lookForRed():
    # set up raspberry pi camera
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 32
    rawCapture = PiRGBArray(camera, size=(640, 480))

    # allow the camera to warmup
    time.sleep(0.1)

    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

        #convert to hsv
        img_frame = frame.array
        hsv = cv2.cvtColor(img_frame, cv2.COLOR_BGR2HSV)

        lower_red = np.array([0,100,100])
        upper_red = np.array([10,255,255])
        lower_red2 = np.array([160,100,100])
        upper_red2 = np.array([179,255,255])

        mask_red_min = cv2.inRange(hsv, lower_red, upper_red)
        mask_red_max = cv2.inRange(hsv, lower_red2, upper_red2)
        red_hue_image = cv2.addWeighted(mask_red_min, 1.0, mask_red_max, 1.0, 0.0)

        if (isRedColor(red_hue_image, percentageOfColorForPhoto)):
            print("photo taken!")
            camera.start_preview()
            # Camera warm-up time
            sleep(1)
            return True
        #need to refresh buffer
        rawCapture.truncate(0)



# # capture frames from the camera
# for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
#
#     #convert to hsv
#     img_frame = frame.array
#     hsv = cv2.cvtColor(img_frame, cv2.COLOR_BGR2HSV)
#     image = rawCapture.array
#
#     # display the image on screen and wait for a keypress
#     cv2.imshow("Image", image)
#
#     sensitivity_red =10
#     lower_red = np.array([0,100,100])
#     upper_red = np.array([10,255,255])
#     lower_red2 = np.array([160,100,100])
#     upper_red2 = np.array([179,255,255])
#
#     mask_red_min = cv2.inRange(hsv, lower_red, upper_red)
#     mask_red_max = cv2.inRange(hsv, lower_red2, upper_red2)
#     red_hue_image = cv2.addWeighted(mask_red_min, 1.0, mask_red_max, 1.0, 0.0)
#     res_red = cv2.bitwise_and(img_frame, img_frame, mask=red_hue_image)
#
#     cv2.imshow('res_red', res_red)
#
#     if (isRedColor(red_hue_image, percentageOfColorForPhoto)):
#         print("photo taken!")
#         camera.start_preview()
#         # Camera warm-up time
#         sleep(2)
#         camera.capture('Red.jpg')
#
#
#     sensitivity_green = 15;
#     lower_green = np.array([60 - sensitivity_green, 100, 50])
#     upper_green = np.array([60 + sensitivity_green, 255, 255])
#
#     mask_green = cv2.inRange(hsv, lower_green, upper_green)
#
#     res_green = cv2.bitwise_and(img_frame, img_frame, mask=mask_green)
#
#     cv2.imshow('res_green', res_green)
#
#     #need to refresh buffer
#     rawCapture.truncate(0)
#
#     k = cv2.waitKey(5) & 0xFF
#     if k == 27:
#         break
# cv2.destroyAllWindows()

