from script import xmlScript as xml
from script import ocr as imageReader
from script import TypingBot as typingBot
from script import LabelClick
from script import SearchBot
from script import ScreenShotBot
from Webcam import imageFromWebcam as getFile
from Label import openFile
import time
import os
oneTime = False
 
def start():
    listOfTrask = xml.readXml('trask', 'main') 
    for trask in listOfTrask:
        if(trask == 'dymo'):
            dymo()
        elif(trask == 'label'):
            labelMaker()
        elif(trask == 'webcam'):
            webcam()
        elif(trask == 'ocr'):
            ocr('webcam')

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
def labelMaker():
    isRunning = True
    index = 0
    while(5 > index and isRunning == True):
        os.system('python script/ButtonsFromArrayGUI.py')
        text = readChooseWordXml()
        if(index == 0):
            writeLabel('customerNumber', text)
        else:
            print(text)
            if(text[0] == "done"):
             while(5 > index):
                 removeLabelText('Produkt'+str(index))
                 isRunning = False
                 index += 1
            else:
                writeLabel('Produkt'+str(index), text)
        index += 1
    printLabel()

def writeLabel(labelTextField, textToEnter):
    objScreen = screenshot('windows')
    objLoc = search(objScreen, labelTextField)
    text = readChooseWordXml()
    click(objLoc)
    writerBot(text)

def removeLabelText(labelTextField):
    objScreen = screenshot('windows')
    objLoc = search(objScreen, labelTextField)
    text = readChooseWordXml()
    click(objLoc)
    spacebar()    

def dymo(): 
    openFile.deleteFile()
    openFile.copyFile()
    openFile.openFile()
    fundet = False
    time.sleep(0.1)
    objScreen = screenshot('windows')
    max_val = SearchBot.check(objScreen, 'newLabelCheck')
    if(max_val >= 0.75):
        objScreen = screenshot('windows')
        objLoc = search(objScreen, 'newLabelNo')
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
    time.sleep(0.5)
    getFile.takeImageFromWebcamFolder()

def spacebar():
    typingBot.spacebar()
def windowsKey():
    typingBot.windowsKey()
def printLabel():
    typingBot.printLabel()

def screenshot(windows):
    return ScreenShotBot.take_screenshot(windows)

def search(imgName, label):
    return SearchBot.find_label(imgName, label)


def click(max_loc):
    LabelClick.Click_coord(max_loc)

def writerBot(text):
    typingBot.type_string_with_delay(text)

def readChooseWordXml():
    word = xml.readXml('choosenword','main')
  
    return word

def ocr(imgName):   
    fileToWrite = 'ocr'
    xml.createXml('ocr',fileToWrite, 'main')
    list = imageReader.listOfWords(imgName)
    list.reverse()
    for f in list:
       xml.saveToXml('ocr',fileToWrite, f, 'main')
    listFromXml = xml.readXml(fileToWrite, 'main')
    return list






