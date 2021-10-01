import sys 
sys.path.append('..\DymoPrint')
from Controller import dymoController as printer
from model import order as ordersM
import time
def printOrder(orders):
    ordersM = orders
    printer.dymoController(orders.customerNO, orders.products, orders.productNos)
    
    
