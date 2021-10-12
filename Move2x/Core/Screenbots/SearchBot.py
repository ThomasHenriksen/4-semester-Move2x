import numpy as np
import cv2 as cv
import pyautogui as pg
import win32com 
import imutils
from ScreenShotBot import image 
#import Screenshotbot as screenshotbot

#pg.screenshot("straight_to_disk.png") #take screenshot and saves ti disk
               

                
#image = cv.imread("straight_to_disk.png") # reads from disk (showing it got a screenshot and it is on desk)
#screenshotimg = Screenshotbot('straight_to_disk.png')

#cv.IMREAD_IMREAD_UNCHANGED
#haystack_img = cv.imread('straight_to_disk.png', cv.IMREAD_REDUCED_COLOR_2) #half size
haystack_img = cv.imread('straight_to_disk.png', cv.IMREAD_UNCHANGED) #half size
needle_img = cv.imread('LabelCustomer.jpg', cv.IMREAD_UNCHANGED)
result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)

min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

print('Best match top left positopn: %s' % str(max_loc))
print('Best match confidence: %s' % str(max_val))

threshold = 0.8
if max_val >= threshold:
    print('Found Dymoimg')

    #get dimensions of the needle image
    needle_w = needle_img.shape[1]
    needle_h = needle_img.shape[0]


    top_left = max_loc
    bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)

    cv.rectangle(haystack_img, top_left, bottom_right, color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)

    cv.imshow('Result', haystack_img)
    x, y = max_loc
    max_loc = x + 20, y + 20
    pg.click(max_loc)
    cv.waitKey()
