import pyodbc
import Model.Product as Product



server = 'tcp:hildur.ucn.dk' 
database = 'dmaa0919_1078101' 
username = 'dmaa0919_1078101' 
password = 'Password1!' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

def selectAllOrders():
    cursor.execute("SELECT * FROM product;") 
    row = cursor.fetchone() 
    while row: 
     b = Product.Product(row[0])
     print(b.ProductInfo)
     row = cursor.fetchone()

def addNewOrder(customerNo, part, color, product, productNo):

    #Sample insert query
    queryString = customerNo, part, color, product, productNo
    ("""INSERT INTO product (customerNo, part, color, product, productNo) 
     VALUES (?,?,?,?,?)""",
    'SQL Server Express New 20', 'SQLEXPRESS New 20', 0, 0, CURRENT_TIMESTAMP).rowcount
    cursor.execute
    cursor.commit()
    print('Rows inserted: ' + str(count))


addNewProduct(customerNo, part, color, product, productNo)

selectAllproducts()