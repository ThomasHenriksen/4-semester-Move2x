import Database.ProductAccess as Access




def saveOrder(customerNo, part, color, product, productNo):

    return Access.addNewOrder(customerNo, part, color, product, productNo)

def getProducts():

    return Access.selectAllOrders()
    

