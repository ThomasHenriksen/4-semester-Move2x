import sys 
sys.path.append('..\ImageReader')
from service import imageReaderService as service
import Database as db
import DymoPrint as printer
from model import order as ordersM

def OcrOrder(path):
    return service.OCR(path)


def saveToDatabase(orders):
    listOfOrder = orders
    for order in listlistOfOrder:
        db.saveToDatabase(order.customerNo, order.part, order.color, order.product, order.productNo)
    
    return null


def printOrder(orders):
    listOfOrder = orders
    for order in listlistOfOrder:
        printer.printOrder(order.customerNo, order.part, order.color, order.product, order.productNo)
    
    return null
