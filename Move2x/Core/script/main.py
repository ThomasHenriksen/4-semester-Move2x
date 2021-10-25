from script import xmlScript as xml
from script import ocr as imageReader
from script import TypingBot as typingBot
from script import LabelClick
from script import SearchBot
from script import ScreenShotBot

import time
import os

 
def start():
    listOfTrask = xml.readXml('trask', 'main')
    objWebcam = ''
    objOcr = []
    objScreen = ''
    objLoc = []   
    for trask in listOfTrask:
        if(trask == 'dymo'):
          objScreen = screenshot('windows')
          objLoc = search(objScreen, 'windows')
          click(objLoc)
          text = ['dymo']
          writerBot(text)
          objScreen = screenshot('windows')
          objLoc = search(objScreen, 'dymo')
          click(objLoc)
        elif(trask == 'label'):
          os.system('python script/ButtonsFromArrayGUI.py')
          objScreen = screenshot('windows')
          objLoc = search(objScreen, 'customerNumber')
          text = readChooseWordXml()
          click(objLoc)
          writerBot(text)
          print(text)
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
          print()
        elif(trask == 'webcam'):
          objScreen = screenshot('windows')
          objLoc = search(objScreen, 'windows')
          click(objLoc)
          text = ['logitech']
          writerBot(text)
          objScreen = screenshot('windows')
          objLoc = search(objScreen, 'webcam')
          click(objLoc)
          time.sleep(20)
          objScreen = screenshot('webcam')
        elif(trask == 'ocr'):
          ocr('webcam')
 
    
def print():
    typingBot.print()

def screenshot(windows):
    return ScreenShotBot.take_screenshot(windows)

def search(imgName, label):
    return SearchBot.find_label(imgName, label)


def click(max_loc):
    LabelClick.Click_coord(max_loc)

def writerBot(text):
    typingBot.type_string_with_delay(text)

def readChooseWordXml():
    return xml.readXml('choosenword','main')

def ocr(imgName):   
    fileToWrite = 'ocr'
    xml.createXml('ocr',fileToWrite, 'main')
    list = imageReader.listOfWords(imgName)
    list.reverse()
    for f in list:
       xml.saveToXml('ocr',fileToWrite, f, 'main')
    listFromXml = xml.readXml(fileToWrite, 'main')
    return list






