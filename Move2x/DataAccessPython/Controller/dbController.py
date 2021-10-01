import Database.ProductAcess
class dbController(object):
    """description of class"""
    #Sample select query
cursor.execute("SELECT @@version;") 
row = cursor.fetchone() 
while row: 
    print(row[0])
    row = cursor.fetchone()

addNewProduct()



