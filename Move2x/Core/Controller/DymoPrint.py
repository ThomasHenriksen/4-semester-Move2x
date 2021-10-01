import sys 
sys.path.append('..\DymoPrint')
from Controller import dymoController as printer
from model import order as ordersM

def printOrder(orders):
    ordersM = orders
    print(ordersM)
    printer.dymoController(orders.customerNO, orders.products, orders.productNos)
    
    return null
