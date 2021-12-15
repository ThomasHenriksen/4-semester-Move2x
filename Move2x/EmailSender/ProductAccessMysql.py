import mysql.connector
from datetime import timedelta
import datetime

mydb = mysql.connector.connect(
  host="WickedGames.asuscomm.com",
  user="Move2x",
  password="!move2x",
  database="b'move2x_dk_db_app'"
)

def getOrderFromDataBase(customer):
    
    mycursor = mydb.cursor()
    sql = "SELECT baseorder.expFinishTime, baseorder.name, baseorderproduct.amount, product.cover, product.fuse, product.id \
     FROM product INNER JOIN baseorderproduct ON product.id = baseorderproduct.fk_product INNER JOIN baseorder ON baseorderproduct.fk_baseorder = baseorder.id \
     WHERE name = '"+customer +"'"
    mycursor.execute(sql)

    data = mycursor.fetchall()

    orderList = []
    for row in data:
        
        orderList.append(dataRow(row))
    
    
    return orderList
def getCustomerFromDataBase():
    
    mycursor = mydb.cursor()
    sql = "SELECT name, expFinishTime FROM baseorder"
    mycursor.execute(sql)

    data = mycursor.fetchall()

    customerList = []
    
    for row in data:
      order = buildCustomer(row)
      order.append(getOrderFromDataBase(order[1]))
      customerList.append(order)

    customerList = sorted(customerList, key = lambda i: i[1])
    return customerList
def buildCustomer(row):
     customerList = []
     

     customer = row[0]

     time_obj = datetime.datetime.strptime(str(row[1]),'%H:%M:%S').time()  
     theTimeExp = str(time_obj)[:5]

     
     customerList.append(theTimeExp)
     customerList.append(str(customer))
     return customerList
def dataRow(row):
    order = []

    

    amount = row[2]
    cover = row[3]
    fuse = row[4]
    productId = row[5]

    order.append(amount)
    order.append(cover)

    if(fuse == 'L' or fuse == 'R'):
         order.append('1 fuse '+fuse)
    elif(fuse == 'L + R'):
         order.append('2 fuses ')
    elif(productId == 6001 or productId == 6002):
         order.append('phone')
    else:
         order.append('no fuses')

    order.append('('+str(productId)+')')

     
     
     
    
    return order
