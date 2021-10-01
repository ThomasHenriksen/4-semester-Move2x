import pyodbc
import Model.Product as Product
from Model import order as orders
import time

server = 'tcp:hildur.ucn.dk' 
database = 'dmaa0919_1078101' 
username = 'dmaa0919_1078101' 
password = 'Password1!' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

def selectAllOrders():
    cursor.execute("SELECT * FROM productOrder;") 
    row = cursor.fetchone() 
    while row: 
     b = Product.Product(row[0])
     print(b.ProductInfo)
     row = cursor.fetchone()

def addNewOrder(order):
    orders = order
    
    #Sample insert query
    queryString = "INSERT INTO productOrder (customerNO, parts, colors, product, productNo) VALUES (?,?,?,?,?)"
    
    list = cursor.execute(queryString, (orders.customerNO, orders.parts, orders.colors, orders.products, orders.productNos))
    cursor.commit()
    

