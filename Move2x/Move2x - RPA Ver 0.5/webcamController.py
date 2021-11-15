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
    fileToWrite = 'ocr2'
    xml.createXml(fileToWrite)
    checkList = []
    i = 0
    
    for img in SearchBot.searchForAutoCrop():
        
        listW = imageReader.listOfWords(img)
        
        os.remove(temp+img+type)
        for b in listW:
            
            if(b !="" and b[0].isdigit()):
                if(len(checkList) != 0):
                    if(b.find(checkList[i-1])):
                        
                        checkList.append(b)          
                        i+=1
                else:
                    checkList.append(b)
                    i+=1

    customer = 1
    order = ''
    clearList = []
    orders = []
    check = False
    orderTime = ''
    for b in checkList:
        
        if(len(b) >2 ):
           
            if(b[2].isdigit()):
              
              try:
                if(customer != int(b[:5])):
                   
                   if(customer == 1):
                     orders = []
                     customer = int(b[:5])
                     orders.append(customer)
                      
                     order = '' 
                   else:
                     clearList.append(orders)
                     orders = []
                     customer = int(b[:5])
                     orders.append(customer)
                 
                     order = '' 
              except:
                   print('fail to covnert b to int')
            else:
              try:
               if(b[2] != ':'):
                  
                  if(order != b):
                    order = b
                    order = order.replace('.', '')
                    order = order.replace('be', 'pc')
                    orders.append(order)
                    x = []
                   # try:
                   #  x = order.split('.')
                   # except:
                   #     x.append(order[:5])
                   #     x.append(order[5:])
                   # orders.append(x[0][0])
                   # orders.append(x[1].lstrip())
               else:
                    if(orderTime != b):
                        orderTime = b
                        orders.insert(1,orderTime)
                     
              except:
                  print('Fail in other')
                  print('Fail in other ' + b)

    clearList.append(orders)   
    
    
      
          
 
        
        
    
    i = 0
    clearList.reverse()
    for f in clearList:
        f = remove_duplicates(f)
        xml.saveToXmlList(f)
                   
            
    testlist = xml.readXml('ocr2') 
    for e in testlist:
        print(e)
    return 'OCR is completion'
def remove_duplicates(l):
    return list(dict.fromkeys(l))

