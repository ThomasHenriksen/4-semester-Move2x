import numpy as np
import cv2 as cv
import pyautogui as pg
import win32com 
import imutils
 
image = pg.screenshot()
image = cv.cvtColor(np.array(image), cv.COLOR_RGB2BGR)

pg.screenshot("straight_to_disk.png") #take screenshot and saves to disk
               

                
image = cv.imread("straight_to_disk.png") # reads from disk (showing it got a screenshot and it is on desk)
