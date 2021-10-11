from script import xml 
from script import ocr as imageReader
from win10toast import ToastNotifier

temp = 'Temp\\'
type = '.jpg'
path = temp + 'last' + type 



def ocr(path):
    fileToWrite = 'ocr'
    xml.createXml('ocr',fileToWrite)
   
    list = imageReader.listOfWords(path)
    list.reverse()
    for f in list:
       xml.saveToXml('ocr',fileToWrite, f)
       
    listFromXml = xml.readXml(fileToWrite)
    print(listFromXml)
  
ocr(path)



#toaster = ToastNotifier()
#toaster.show_toast("Demo notification",
#                   "Hello world",
#                   duration=10)

