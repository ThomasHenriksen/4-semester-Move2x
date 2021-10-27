from script import xmlScript as xml
from script import ocr as imageReader
from script import TypingBot as typingBot
from script import LabelClick
from script import SearchBot
from script import ScreenShotBot
from script import imageFromWebcam as getFile
from script import openFile
import time
import os
oneTime = False
 
def start():
    listOfTrask = xml.readXml('trask', 'main')
    objWebcam = ''
    objOcr = []
    objScreen = ''
    objLoc = []   
    for trask in listOfTrask:
        if(trask == 'dymo'):
            takePicture()
            #dymo()
        elif(trask == 'label'):
            takePicture()
            #label()
        elif(trask == 'webcam'):
            takePicture()
            #webcam()
        elif(trask == 'ocr'):
            takePicture()
            #ocr('webcam')

def webcam():
     windowsKey()
     text = ['logitech']
     writerBot(text)
     objScreen = screenshot('windows')
     objLoc = search(objScreen, 'webcam')
     click(objLoc)
     time.sleep(20)
     
def label():
    os.system('python script/ButtonsFromArrayGUI.py')
    objScreen = screenshot('windows')
    objLoc = search(objScreen, 'customerNumber')
    text = readChooseWordXml()
    click(objLoc)
    writerBot(text)
    os.system('python script/ButtonsFromArrayGUI.py')
    objScreen = screenshot('windows')
    objLoc = search(objScreen, 'produkt1')
    text = readChooseWordXml()
    click(objLoc)
    writerBot(text)
    os.system('python script/ButtonsFromArrayGUI.py')
    objScreen = screenshot('windows')
    objLoc = search(objScreen, 'produkt2')
    text = readChooseWordXml()
    click(objLoc)
    writerBot(text)
    os.system('python script/ButtonsFromArrayGUI.py')
    objScreen = screenshot('windows')
    objLoc = search(objScreen, 'produkt3')
    text = readChooseWordXml()
    click(objLoc)
    writerBot(text)
    os.system('python script/ButtonsFromArrayGUI.py')
    objScreen = screenshot('windows')
    objLoc = search(objScreen, 'produkt4')
    text = readChooseWordXml()
    click(objLoc)
    writerBot(text)
    printLabel()

def dymo(): 
    openFile.deleteFile()
    openFile.copyFile()
    openFile.openFile()
    fundet = False
    time.sleep(0.4)
    objScreen = screenshot('windows')
    max_val = SearchBot.check(objScreen, 'newLabelCheck')
    if(max_val >= 0.75):
        objScreen = screenshot('windows')
        objLoc = search(objScreen, 'newLabelNo')
        click(objLoc)


def takePicture():
    fundet = False
    while(fundet == False):
        objScreen = screenshot('windows')
        max_val = SearchBot.check(objScreen, 'WebcamCheck')
        if(max_val >= 0.75):
            fundet = True
    objScreen = screenshot('windows')
    objLoc = search(objScreen, 'takePicture')
    click(objLoc)
    time.sleep(0.1)
    getFile.takeImageFromWebcamFolder()

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






