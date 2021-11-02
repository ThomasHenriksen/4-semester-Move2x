from script import openFile
from script import LabelClick
from script import SearchBot
from script import ScreenShotBot
from script import TypingBot as typingBot
from script import ocr as imageReader
from script import xmlScript as xml
import time
import os



def labelMaker():
    isRunning = True
    index = 0
    while(5 > index and isRunning == True):
        time.sleep(0.5)
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
    return 'Print completion'

def exitLabel():
    objScreen = screenshot('windows')
    objLoc = search(objScreen, 'exitLabel')
    click(objLoc)
    time.sleep(0.7)
    max_val = SearchBot.check(objScreen, 'newLabelCheck')
    if(max_val >= 0.75):
        objScreen = screenshot('windows')
        objLoc = search(objScreen, 'newLabelNo')
        click(objLoc)
    return False

def writeLabel(labelTextField, textToEnter):
    objScreen = screenshot('windows')
    objLoc = search(objScreen, labelTextField)
    text = readChooseWordXml()
    click(objLoc)
    writerBot(text)
    return False

def removeLabelText(labelTextField):
    objScreen = screenshot('windows')
    objLoc = search(objScreen, labelTextField)
    text = readChooseWordXml()
    click(objLoc)
    spacebar()
    return False

def dymo(): 
    openFile.deleteFile()
    openFile.copyFile()
    openFile.openFile()
    fundet = False
    
    i = 0
    while(i < 2 and fundet == False):
        time.sleep(0.1)
        objScreen = screenshot('windows')
        max_val = SearchBot.check(objScreen, 'newLabelNo')
        print('here')
        if(max_val >= 0.75):
            objScreen = screenshot('windows')
            objLoc = search(objScreen, 'newLabelNo')
            click(objLoc)
            fundet = True
        i+= 1
    return 'Dymo is open'

def spacebar():
    return typingBot.spacebar()

def windowsKey():
    return typingBot.windowsKey()

def printLabel():
    return typingBot.printLabel()

def screenshot(windows):
    return ScreenShotBot.take_screenshot(windows)

def search(imgName, label):
    return SearchBot.find_label(imgName, label)

def click(max_loc):
    return LabelClick.Click_coord(max_loc)

def writerBot(text):
    return typingBot.type_string_with_delay(text)

def readChooseWordXml():
    word = xml.readXml('choosenword')
  
    return word



