from script import LabelClick
from script import SearchBot
from script import ScreenShotBot
from script import imageFromWebcam as getFile
from script import TypingBot as typingBot
import time
import os

def start():
    webcam()

def windowsKey():
    typingBot.windowsKey()


def screenshot(windows):
    return ScreenShotBot.take_screenshot(windows)

def search(imgName, label):
    return SearchBot.find_label(imgName, label)

def click(max_loc):
    LabelClick.Click_coord(max_loc)

def writerBot(text):
    typingBot.type_string_with_delay(text)

def webcam():
     windowsKey()
     text = ['logitech']
     time.sleep(0.1)
     writerBot(text)
     objScreen = screenshot('windows')
     objLoc = search(objScreen, 'logi')
     click(objLoc)
     takePicture()
     objLoc = search(objScreen, 'closeWebCam')
     click(objLoc)

def takePicture():
    fundet = False
    while(fundet == False):
        print('waiting')
        objScreen = screenshot('windows')
        max_val = SearchBot.check(objScreen, 'WebcamCheck')
        if(max_val >= 0.75):
            fundet = True
    objScreen = screenshot('windows')
    objLoc = search(objScreen, 'takePicture')
    click(objLoc)
    time.sleep(0.2)
    getFile.takeImageFromWebcamFolder()