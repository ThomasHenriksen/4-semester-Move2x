import sys 
sys.path.append('..\ImageReader')
from service import imageReaderService as service
import DataBase as db
import DymoPrint as printer
from model import order as ordersM

def OcrOrder(path):
    return service.OCR(path)


def saveToDatabase(orders):
    ordersM = orders
    listOfOrder = ordersM
    for order in listOfOrder:
       db.saveToDatabase(order)
    
    return 'test'


def printOrder(orders):
   ordersM = orders
   listOfOrder = ordersM
   print(ordersM)
   for order in listOfOrder:
        printer.printOrder(order)
    
   return 'test'
