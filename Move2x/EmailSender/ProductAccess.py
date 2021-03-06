import pyodbc
import time
import datetime
server = 'tcp:hildur.ucn.dk' 

database = 'dmaa0919_1078101'

username = 'dmaa0919_1078101' 
password = 'Password1!' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
    
def connect():
    server1 = 'DESKTOP-ULH1RFG' 
    server2 = 'LAPTOP-K8V4GCVI\SQLEXPRESS'
    server3 = 'DESKTOP-KE3U8FV'
    database = 'move2x_dk_db_app' 
    #password = '210210ht' 
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      'Server=' + server1 + ';'
                      'Database=move2x_dk_db_app;'
                      'Trusted_Connection=yes;')
    cursor = cnxn.cursor()
    return cursor

def getOrderFromDataBase():
    cursor = connect()
    # assuming that Tags table is in dbo schema
    selectData = 'SELECT  dbo.baseorder.expFinishTime, dbo.baseorder.name, dbo.baseorderproduct.amount, dbo.product.cover, dbo.product.fuse, dbo.product.id '
    fromData = 'FROM dbo.product INNER JOIN dbo.baseorderproduct ON dbo.product.id = dbo.baseorderproduct.fk_product INNER JOIN dbo.baseorder ON dbo.baseorderproduct.fk_baseorder = dbo.baseorder.id'
    query = selectData + fromData

    cursor.execute(query)
    row = cursor.fetchone()
    orderList = []
    while row:
     order = []

     timeExp = row[0]
     try:
         theTimeExp = timeExp.strftime("%H:%M")
     except:
         theTimeExp = timeExp[:5]

     customer = row[1]
     amount = row[2]
     cover = row[3]
     fuse = row[4]
     productId = row[5]

     order.append(theTimeExp)
     order.append(customer)
     order.append(amount)
     order.append(cover)

     if(fuse == 'L' or fuse == 'R'):
         order.append('1 fuse '+fuse)
     elif(fuse == 'L + R'):
         order.append('2 fuses ')
     elif(productId == 6001 or productId == 6002):
         order.append('phone')
     else:
         order.append('fuses '+fuse)

     order.append('('+str(productId)+')')

     orderList.append(order)
     
     row = cursor.fetchone()
    
    return orderList
    

ordlist = getOrderFromDataBase()
for b in ordlist:
    print(b)
