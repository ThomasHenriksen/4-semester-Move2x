"""
This script is used for C.R.U.D for XML

Made by 
@BJARKE ROBERT STØVE ANDERSØN
@CHRISTIAN MARC JØRGENSEN
@MAGNUS SØRENSEN 
@THOMAS HENRIKSEN  
"""
from xml.dom import minidom
from xml.etree import ElementTree

import os 

"""
This method is used for creating the XML file

Parameters:
-toFile (--toFile): inputs the name of the file
"""
def createXml(toFile):
    
    root = minidom.Document()
    xml = root.createElement('root')
    root.appendChild(xml)
    productChild = root.createElement('test')
    xml_str = root.toprettyxml(indent = "\t")
    path_file = 'XML\_'+ toFile + '.xml'
    with open(path_file, "w") as f:
        f.write(xml_str)

"""
This method is used for making the XML file more readable

Example of a element:

  <Order nr="10011">
    <Customer>10011</Customer>
  <Time>00:40</Time>
  <ProductOrder Amount="1" Status="Cancel" orderId="10011 Blue phone (6002)">
      <Amount>1</Amount>
    <Product>Blue phone (6002)</Product>
    </ProductOrder>
  </Order>

Parameters:
-elem (--elem): input XML element
-level=0 (--level=0): inputs the level of the element it's on

Return:

-elem (--elem): outputs the element
"""
def indent(elem, level=0):
    i = "\n" + level*"  "
    j = "\n" + (level-1)*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
           elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
           elem.tail = i
        for subelem in elem:
           indent(subelem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = j
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = j
    return elem

"""
This method is used to determined how to save the order

Example:

orderList(time, customer, productOrder((amount, product)))
or
orderList(time, customer, (amount, product))

Parameters:
-orderList (--list): inputs a list that contains raw data of orders
"""
def saveOrder(orderList):
    time = orderList[0]
    customer = orderList[1]
    productOrder = orderList[2]
    amount = ''
    product = ''
    
    if isinstance(productOrder, list): #Checks if the productOrder is a list
        for item in productOrder: #for each productOrder there is in the list
            amount = item[:1] #Splits the item(amount) up to index 1 
            product = item[2:] #Splits the item(product) from index 2
            if(product[:2] == 'pc'): #Checks if PC is the first that is listed in product
                #Splits the product from index 3, removes all empty spaces before and after the text, then capitalizes the first letter
                product = product[3:].lstrip().capitalize().rstrip() 
                index = len(product)
                if(product[index-8] == 'r' or product[index-8] == 'l'): #Looks for r or l
                    product = product[:index-8] +  product[index-8].upper()+product[index-7:] #Makes r or l capitalized

            found = findOrderXml('ocr', str(customer) + ' ' + product) #Tries to find order in XML file
        
            if not found:

                saveToXml(time,customer,amount,product) #calls the method saveToXml

    else:  
        amount = productOrder[:1] #references the comment in line 92
        product = productOrder[2:].capitalize().rstrip() #references the comment in line 93

        index = len(product)
        if(product[index-8] == 'r' or product[index-8] == 'l'): #references the comment in line 98
           product = product[:index-8] +  product[index-8].upper()+product[index-7:] #references the comment in line 99
        
        found = findOrderXml('ocr', customer + ' ' + product) #references the comment in line 101


        if not found:
            saveToXml(time,customer,amount,product) #references the comment in line 105

"""
This method is used to saving the XML file

Parameters:
-time (--string): inputs the time
-customer (--int): inputs the customer
-amount (--int): inputs the amount
-product (--string): inputs the product
"""
def saveToXml(time,customer,amount,product):
    path_file = 'XML\_ocr.xml'
    root = ElementTree.parse(path_file).getroot()
    
    c = ElementTree.Element('Order')
    
    customerXml = ElementTree.SubElement(c, 'Customer')
    customerXml.text = str(customer) 
    c.set('nr',customerXml.text)    
       
    orderTime = ElementTree.SubElement(c, 'Time')
    orderTime.text = str(time)

    productOrder = ElementTree.SubElement(c,'ProductOrder')

    productXml = ElementTree.SubElement(productOrder,'Amount')
    productXml.text = str(amount)
    productXml = ElementTree.SubElement(productOrder,'Product')
    productXml.text = str(product)
    productOrder.set('orderId',customerXml.text +' '+ productXml.text )
    productOrder.set('Status','Waiting' )
    productOrder.set('Amount', str(amount))
        
    
    root.insert(0, c)
    tree = ElementTree.ElementTree(indent(root))
    tree.write(path_file, xml_declaration=True, encoding='utf-8')

"""
This method is used for reading the XML file

Parameters:
-toFile (--toFile): inputs the name of the file

Return:
-orderList (--list): outputs a list of orders
"""
def readOrderXml(toFile):
    path_file = 'XML\_'+ toFile + '.xml'
    tree = ElementTree.parse(path_file)
    root = tree.getroot()
    
    orderList = []

    for order in root.findall('Order'):
        try:
            orderList.append(buildOrder(order))
        except:
            dontdoany = ''
    return orderList


def readXml(toFile):
    path_file = 'XML\_'+ toFile + '.xml'
    tree = ElementTree.parse(path_file)
    root = tree.getroot()
    data = []
    for elem in root.iter('OCR'):
        data.append(elem.text) 
      
    return data   

"""
This method is used for finding and changing the status of the given orders

Parameters:
-toFile (--toFile): inputs the name of the file
-orderFind (--string): inputs name of the order
-Status (--string): inputs the status
"""
def changeStatusOnOrderXml(toFile, orderFind,status):
    path_file = 'XML\_'+ toFile + '.xml'
    tree = ElementTree.parse(path_file)
    root = tree.getroot()
    orders = root.findall('.//ProductOrder')
    
    for order in orders:
        value = order.get('orderId') 
        
        if(orderFind == value ):
            order.set('Status',status)
    
    tree = ElementTree.ElementTree(indent(root))
    tree.write(path_file, xml_declaration=True, encoding='utf-8')

"""
This method is used for checking if the order is in the XML file

Parameters:
-toFile (--toFile): inputs the name of the file
-orderFind (--string): inputs name of the order

Return:
-find (--bool): outputs true or false
"""
def findOrderXml(toFile, orderFind):
    find = False

    path_file = 'XML\_'+ toFile + '.xml'
    tree = ElementTree.parse(path_file)
    root = tree.getroot()
    orders = root.findall('.//ProductOrder')
    
    for order in orders:
        value = order.get('orderId') 
        if(orderFind == value ):
            find = True
    
    return find

"""
This method is used to build the list of orders

Return:
-s (--list): outputs a list of orders
"""
def getOrder():
        orderList = readOrderXml('ocr')
        order = []
        for o in orderList:     
            status = o[0]
            product = o[4]
            if(status == 'Done' or status == 'Cancel'):
                lala = '2' #does nothing
      
            else:
                order.append(o)
        if(len(order) == 0): #if there is no order, makes a empty order
            noOrder=[]
            noOrder.append('')
            noOrder.append('000000')
            noOrder.append('')
            noOrder.append('1')
            noOrder.append('No Order')
            order.append(noOrder)
        order = sorted(order, key = lambda i: i[2])
        s = []
        for i in order: #Removes any double orders
             if i not in s:
                 s.append(i)
        return s

"""
This method is used for building the order from the XML file

Parameters:
-order (--list): inputs list of strings

Return:
-data (--list): outputs a full order
"""
def buildOrder(order):
    data = []
    
    customer = order.find('Customer').text
    if(len(customer)<5):
        int(customer+'fd') #throws a exception
    orderTime = order.find('Time').text
    status = order.findall('ProductOrder')

    for productOrder in status:
        status = productOrder.get('Status')      
        amount = productOrder.get('Amount')
        if int(amount):
            amount = amount
        productText = productOrder[1].text
        data.append(status)
        data.append(customer)
        data.append(orderTime)
        data.append(amount)
        data.append(productText)
        
        
    return data
