import pyodbc
import Model.Product as Product


server = 'tcp:hildur.ucn.dk' 
database = 'dmaa0919_1078101' 
username = 'dmaa0919_1078101' 
password = 'Password1!' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

def selectAllproducts():
    cursor.execute("SELECT * FROM product;") 
    row = cursor.fetchone() 
    while row: 
     b = Product.Product(row[0])
     print(b.ProductInfo)
     row = cursor.fetchone()

def addNewProduct(description):

    #Sample insert query
    cursor.execute
    ("""INSERT INTO product (id, productNo, productInfo, numberOfProducts) 
     VALUES (?,?,?,?)""",
    'SQL Server Express New 20', 'SQLEXPRESS New 20', 0, 0, CURRENT_TIMESTAMP).rowcount 
    cnxn.commit()
    print('Rows inserted: ' + str(count))



selectAllproducts()