#This script is used for controlling printing and navigating the controls for the label

#Made by 
#@BJARKE ROBERT ST�VE ANDERS�N
#@CHRISTIAN MARC J�RGENSEN
#@MAGNUS S�RENSEN 
#@THOMAS HENRIKSEN  

from script import openFile
from script import LabelClick
from script import SearchBot
from script import ScreenShotBot
from script import TypingBot as typingBot
from script import ocr as imageReader
from script import xmlScript as xml
import time
import os

"""
This method is used to print the label in the DYMO Label Software

Parameters:
-customer (--string): inputs a string containing the customer
-time (--string): inputs a string containing the time
-product (--string): inputs a string containing the product
-amount (--int): inputs the amount of prints
"""
def labelMaker(customer, time, product, amount):
    size = int(amount)   
    i = 0

    found = False
    dymo()
    while(found == False):
        objScreen = screenshot('windows')
        max_val = SearchBot.check(objScreen, 'customerNumber')
       
        if(max_val >= 0.75):
            found = True
    if(found):
       writeLabel('customerNumber', customer)
       writeLabel('Time', time)
       writeLabel('Produkt1', product)
       while(i < size):
             printLabel()
             i+=1
    return 'Print completion'

"""
This method is used to cancel the save for label
"""
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

"""
This method is used for typing out the sentence
Parameters:
-labelTextField (--string): inputs a string containing the name of the field
-textToEnter (--string): inputs a string containing the text to write
"""
def writeLabel(labelTextField, textToEnter):
    objScreen = screenshot('windows')
    objLoc = search(objScreen, labelTextField)
    click(objLoc)
    writerBot(textToEnter)

"""
This method is used for deleting the old template and make a new template by copy it from the backup 
and open the DYMO Label Software
"""
def dymo(): 
    openFile.deleteFile()
    openFile.copyFile()
    openFile.openFile()
    found = False
    
    i = 0
    while(i < 5 and found == False):
        
        objScreen = screenshot('windows')
        max_val = SearchBot.check(objScreen, 'newLabelNo')
        
        if(max_val >= 0.75):
            objScreen = screenshot('windows')
            objLoc = search(objScreen, 'newLabelNo')
            click(objLoc)
            found = True
        i += 1
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



