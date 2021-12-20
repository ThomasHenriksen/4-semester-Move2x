from script import LabelClick
from script import SearchBot
from script import ScreenShotBot
from script import imageFromWebcam as getFile
from script import TypingBot as typingBot
from script import ocr as imageReader
from script import xmlScript as xml
from script import autoAlignImage
import time
import os
import re
from collections import Counter

#This is the script used for business logic for images

#Made by 
#@BJARKE ROBERT STØVE ANDERSØN
#@CHRISTIAN MARC JØRGENSEN
#@MAGNUS SØRENSEN 
#@THOMAS HENRIKSEN 

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
     found = False
     objScreen = screenshot('windows')
     max_val = SearchBot.check(objScreen, 'takePicture')
     if(max_val >= 0.75):
       found = True
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
    index = 0
    while(index < 2):
        found = False
        while(found == False):

            objScreen = screenshot('windows')
            max_val = SearchBot.check(objScreen, 'takePicture')
            if(max_val >= 0.75):
                found = True
        objScreen = screenshot('windows')
        objLoc = search(objScreen, 'takePicture')
        click(objLoc)
        time.sleep(0.2)
        getFile.takeImageFromWebcamFolder()
        index += 1
    return 'img is completion'

def alignPicture():
    autoAlignImage.alignImages()
    return 'Aligning image'

def saveXml(order):
    xml.saveOrder(order)

def ocr():   
    for img in SearchBot.searchForAutoCrop():
        order = imageReader.OCR(img)
        os.remove('Temp\\'+img+'.png')
        if order:
            saveXml(order)
        
    return 'OCR is completion'



