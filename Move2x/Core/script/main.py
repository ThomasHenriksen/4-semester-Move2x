from script import xml 
from script import ocr as imageReader
from script import webcam 
from script import typingBot
from script import LabelClick
from script import SearchBot
from script import ScreenShotBot


from win10toast import ToastNotifier
import threading
import time
import logging

exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter

   def run(self):
      if(self.name == "Thread-1"):
          webcam.startWebcam()
          print_time(self.name, 1, self.counter)
          
      if(self.name == "Thread-2"):
          listOfTrask = xml.readXml('trask')
          time.sleep(5)
          objWebcam = ''
          objOcr = []
          objScreen = ''
          objLoc = []
          for trask in listOfTrask:
              if(trask == 'webcam'):
                  objWebcam = webcam.takePicture()
              elif(trask == 'ocr'):
                  objOcr = ocr(objWebcam)    
              elif(trask == 'click'):
                  click(objLoc)
              elif(trask == 'tast'):
                  writerBot(objOcr)
              elif(trask == 'screen'):
                  objScreen = screenshot()   
              elif(trask == 'search'):
                 objLoc = search(objScreen)             
          webcam.stopWebcam()
          print_time(self.name, 1, self.counter)    

def print_time(threadName, counter, delay):
   while counter:
      if exitFlag:
         threadName.exit()
      counter -= 1
      
def start():
   #toaster = ToastNotifier()
   #toaster.show_toast("Move2x", "Running RPA", duration=120)
    # Create new threads
    exec(open("script\\ButtonsFromArrayGUI").read())
    thread1 = myThread(1, "Thread-1", 1)
    thread2 = myThread(2, "Thread-2", 2)

    # Start new Threads
    thread1.start()
    thread2.start()

def screenshot():
    return ScreenShotBot.take_screenshot()

def search(imgName):
    temp = 'Temp\\'
    type = '.jpg'
    path = temp + imgName + type 
    fileToWrite = 'ocr'
    xml.createXml('ocr',fileToWrite)
    loc = SearchBot.find_label()
    for f in list:
       xml.saveToXml('ocr',fileToWrite, f)

def click(max_loc):
    LabelClick.Click_coord(max_loc)

def writerBot(text):
    typingBot.type_string_with_delay(text)

def ocr(imgName):
    temp = 'Temp\\'
    type = '.jpg'
    path = temp + imgName + type 
    fileToWrite = 'ocr'
    xml.createXml('ocr',fileToWrite)
   
    list = imageReader.listOfWords(path)
    list.reverse()
    for f in list:
       xml.saveToXml('ocr',fileToWrite, f)
       
    listFromXml = xml.readXml(fileToWrite)
    print(listFromXml)
    return list





