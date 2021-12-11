from xml.dom import minidom
from xml.etree import ElementTree

import os 

def createXml(toFile):
    
    root = minidom.Document()
    xml = root.createElement('root')
    root.appendChild(xml)
    productChild = root.createElement('test')
    xml_str = root.toprettyxml(indent = "\t")
    path_file = 'XML\_'+ toFile + '.xml'
    with open(path_file, "w") as f:
        f.write(xml_str)

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

def saveOrder(orderList):
    time = orderList[0]
    customer = orderList[1]
    productOrder = orderList[2]
    amount = ''
    product = ''
    
    if isinstance(productOrder, list):
        for item in productOrder:
            amount = item[:1]
            product = item[2:]
            if(product[:2] == 'pc'):
                product = product[3:].lstrip().capitalize().rstrip()
                index = len(product)
                if(product[index-8] == 'r' or product[index-8] == 'l'):
                    product = product[:index-8] +  product[index-8].upper()+product[index-7:]

            fundet = findOrderXml('ocr', str(customer) + ' ' + product)
        
            if not fundet:

                saveToXml(time,customer,amount,product)

    else:  
        amount = productOrder[:1]
        product = productOrder[2:].capitalize().rstrip() 

        index = len(product)
        if(product[index-8] == 'r' or product[index-8] == 'l'):
           product = product[:index-8] +  product[index-8].upper()+product[index-7:]
        
        fundet = findOrderXml('ocr', customer + ' ' + product)


        if not fundet:
            saveToXml(time,customer,amount,product)


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

def readOrderXml(toFile):
    path_file = 'XML\_'+ toFile + '.xml'
    tree = ElementTree.parse(path_file)
    root = tree.getroot()
    
    dataList = []

    for order in root.findall('Order'):
        try:
            dataList.append(buildOrder(order))
        except:
            dontdoany = ''
    return dataList
    
def readXml(toFile):
    path_file = 'XML\_'+ toFile + '.xml'
    tree = ElementTree.parse(path_file)
    root = tree.getroot()
    data = []
    for elem in root.iter('OCR'):
        data.append(elem.text) 
      
    return data   

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
def getOrder():
        orderList = readOrderXml('ocr')
        orderL = []
        for b in orderList:
            
            if(len(b) > 5):
               orderL.append(b[:5])
               orderL.append(b[5:])
            else:
               orderL.append(b)
        order = []
        for o in orderL:
            
            status = o[0]
            
            product = o[4]
            
            if(status == 'Done' or status == 'Cancel'):
                lala = '2'
                
                
            else:

                order.append(o)
        if(len(order) == 0):
            test=[]
            test.append('')
            test.append('000000')
            test.append('')
            test.append('1')
            test.append('No Order')
            order.append(test)
        order = sorted(order, key = lambda i: i[2])
        s = []
        for i in order:
             if i not in s:
                 s.append(i)
        return s
def buildOrder(order):
    data = []
    
    customer = order.find('Customer').text
    if(len(customer)<5):
        int(customer+'fd')
    orderTime = order.find('Time').text
    status = order.findall('ProductOrder')

    for productOrder in status:
        status = productOrder.get('Status')      
        amount = productOrder.get('Amount')    
        productText = productOrder[1].text
        data.append(status)
        data.append(customer)
        data.append(orderTime)
        data.append(amount)
        data.append(productText)
        
        
    return data
