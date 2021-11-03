from script import LabelClick
from script import SearchBot
from script import ScreenShotBot
from Webcam import imageFromWebcam as getFile
from script import TypingBot as typingBot
from script import ocr as imageReader
from script import xmlScript as xml
from script import autoAlignImage
import time
import os
import re


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

def alignPicture():
    autoAlignImage.alignImages()
    return 'Aligning image'

def ocr():  
    temp = 'temp\\'
    type = '.png'
    listOfWords = []
    fileToWrite = 'ocr'
    xml.createXml('ocr',fileToWrite, 'main')
    checkList = []
    i = 0
    for img in SearchBot.searchForAutoCrop():
        list = imageReader.listOfWords(img)
        os.remove(temp+img+type)
        for b in list:
            if(b !="" and b[0].isdigit()):
                if(len(checkList) != 0):
                    if(b.find(checkList[i-1])):
                        checkList.append(b)          
                        i+=1
                else:
                    checkList.append(b)
                    i+=1
    print('')
    print('new list checkList')
    print('')
    customer = 1
    order = ''
    clearList = []
    check = False

    for b in checkList:
        
        if(b[2].isdigit()):
            if(customer != int(b)):
                customer = int(b)
                clearList.append(customer)
                check = True
                order = ''
                
        else:
            if(b[2] != ':'):
                if(order != b):
                    order = b
                    if(check):
                        x = order.split('.')
                        clearList.append(x[0][0])
                        clearList.append(x[1].lstrip())
                    
    for b in clearList:
        print(b)
   
    #print(testing)

    #for f in list:
   #    xml.saveToXml('ocr',fileToWrite, f, 'main')
    return 'OCR is completion'