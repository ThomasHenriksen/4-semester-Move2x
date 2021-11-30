import Database.ProductAccess as Access




def saveOrder(order):

    return Access.addNewOrder(order)

def getProducts():

    return Access.selectAllOrders()
    

list = getProducts()
print(list)