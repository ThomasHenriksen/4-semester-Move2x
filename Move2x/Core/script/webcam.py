from cv2 import *
from PIL import Image, ImageTk
import time

vc = cv2.VideoCapture(0)

def startWebcam():
    vc.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    vc.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    if vc.isOpened(): # try to get the first frame
         rval, frame = vc.read()
    else:
         rval = False

    while rval:
          rval, frame = vc.read()
          


        
def takePicture():
    
    rval, frame = vc.read()
    cv2.imwrite("Temp\\move2xGameCard.jpg",frame)
     
def stopWebcam():
    vc.release()