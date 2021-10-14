import sys 
sys.path.append('..\DataAccessPython')
from Controller import dbController as db
from model import order as ordersM
def saveToDatabase(orders):
    return db.saveOrder(orders)

def getOrderFromDatabase():
    return db.getAllOrders()