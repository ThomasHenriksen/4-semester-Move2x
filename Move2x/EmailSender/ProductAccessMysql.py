import mysql.connector
from datetime import timedelta
import datetime

mydb = mysql.connector.connect(
  host="WickedGames.asuscomm.com",
  user="Move2x",
  password="!move2x",
  database="b'move2x_dk_db_app'"
)

def getOrderFromDataBase():
    
    mycursor = mydb.cursor()
    sql = "SELECT  baseorder.expFinishTime, baseorder.name, baseorderproduct.amount, product.cover, product.fuse, product.id \
     FROM product INNER JOIN baseorderproduct ON product.id = baseorderproduct.fk_product INNER JOIN baseorder ON baseorderproduct.fk_baseorder = baseorder.id"
    mycursor.execute(sql)

    data = mycursor.fetchall()

    orderList = []
    
    for row in data:
        orderList.append(dataRow(row))
    orderList = sorted(orderList, key = lambda i: i[0])
    return orderList

def dataRow(row):
     order = []


     time_obj = datetime.datetime.strptime(str(row[0]),'%H:%M:%S').time()  
     theTimeExp = str(time_obj)[:5]
     
     
         
         

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
         order.append('no fuses')

     order.append('('+str(productId)+')')

     
     
     
    
     return order
