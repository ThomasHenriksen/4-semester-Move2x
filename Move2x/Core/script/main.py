from script import xmlScript as xml
from script import ocr as imageReader

from script import TypingBot as typingBot
from script import LabelClick
from script import SearchBot
from script import ScreenShotBot


import threading
import time
import logging
import os

exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter

   def run(self):
      if(self.name == "Thread-1"):
          
          print_time(self.name, 1, self.counter)
          
      if(self.name == "Thread-2"):
          listOfTrask = xml.readXml('trask')
          time.sleep(5)
          objWebcam = ''
          objOcr = []
          objScreen = ''
          objLoc = []
         
          
          for trask in listOfTrask:
              if(trask == 'click'):
                  click(objLoc)
              elif(trask == 'tast'):
                  os.system('python script/ButtonsFromArrayGUI.py')
                  text = readChooseWordXml()
                  writerBot(text)

                  
              elif(trask == 'screen'):
                  objScreen = screenshot()   
              
              elif(trask == "textbox"):
                    objLoc = search(objScreen, 'textbox')
              elif(trask == "label"):
                    objLoc = search(objScreen, 'label')
              elif(trask == "windows"):
                    objLoc = search(objScreen, 'windows')
                    click(objLoc)
                    
              elif(trask == "dymo"):
                     writerBot('dymo')
                     objScreen = screenshot()
                     objLoc = search(objScreen, 'dymo')
                     click(objLoc)
              elif(trask == "webcam"):
                    writerBot('logitech')
                    objScreen = screenshot()
                    objLoc = search(objScreen, 'webcam')
                    click(objLoc)
          
          print_time(self.name, 1, self.counter)    

def print_time(threadName, counter, delay):
   while counter:
      if exitFlag:
         threadName.exit()
      counter -= 1
      
def start():
    # Create new threads
    objScreen = screenshot('windows')
    objLoc = search(objScreen, 'windows')
    click(objLoc)
    text = ['', 'dymo']
    writerBot(text)
    objScreen = screenshot('windows')
    objLoc = search(objScreen, 'dymo')
    click(objLoc)
    time.sleep(10)
    i = 0
    while(i < 5):
        objScreen = screenshot('windows')
        objLoc = search(objScreen, 'textbox')
        #os.system('python script/ButtonsFromArrayGUI.py')
        text = readChooseWordXml()
        click(objLoc)
        writerBot(text)
        i += 1


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
    temp = 'Temp\\'
    type = '.png'
    path = temp + imgName + type 
    fileToWrite = 'ocr'
    xml.createXml('ocr',fileToWrite, 'main')
   
    list = imageReader.listOfWords(path)
    list.reverse()
    for f in list:
       xml.saveToXml('ocr',fileToWrite, f, 'main')
       
    listFromXml = xml.readXml(fileToWrite, 'main')
    print(listFromXml)
    return list





