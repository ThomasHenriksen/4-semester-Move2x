import sys 
sys.path.append('..\DataAccessPython')
from Controller import dbController as db

def saveToDatabase(orders):
    listOfOrder = orders
    for order in listlistOfOrder:
        db.save(order)
    
    return null

def getOrderFromDatabase():
    return db.getAllOrders()