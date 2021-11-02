from script import LabelClick
from script import SearchBot
from script import ScreenShotBot
from Webcam import imageFromWebcam as getFile
from script import TypingBot as typingBot
from script import ocr as imageReader
from script import xmlScript as xml
import time
import os



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
     fundet = False
     objScreen = screenshot('windows')
     max_val = SearchBot.check(objScreen, 'takePicture')
     if(max_val >= 0.75):
       fundet = True
     else:
         windowsKey()
         text = ['logitech']
         time.sleep(0.1)
         writerBot(text)
         objScreen = screenshot('windows')
         objLoc = search(objScreen, 'logi')
         click(objLoc)
     return 'Webcam is open'

def takePicture():
    fundet = False
    while(fundet == False):
        print('waiting')
        objScreen = screenshot('windows')
        max_val = SearchBot.check(objScreen, 'takePicture')
        if(max_val >= 0.75):
            fundet = True
    objScreen = screenshot('windows')
    objLoc = search(objScreen, 'takePicture')
    click(objLoc)
    time.sleep(0.2)
    getFile.takeImageFromWebcamFolder()
    return 'img is completion'

    

def ocr():   
    fileToWrite = 'ocr'
    xml.createXml('ocr',fileToWrite, 'main')
    list = imageReader.listOfWords()
    list.reverse()
    for f in list:
       xml.saveToXml('ocr',fileToWrite, f, 'main')
    return 'OCR is completion'