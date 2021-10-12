from script import xml 
from script import ocr as imageReader
from script import webcam 
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
          time.sleep(5)
          webcam.takePicture()
          webcam.stopWebcam()
          print_time(self.name, 2, self.counter)

def print_time(threadName, counter, delay):
   while counter:
      if exitFlag:
         threadName.exit()
      counter -= 1
      

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()






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



toaster = ToastNotifier()
toaster.show_toast("Demo notification",
                   "Hello world",
                   duration=10)

