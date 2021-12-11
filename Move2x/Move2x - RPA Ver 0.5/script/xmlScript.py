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

def saveToXml(toFile,words):
    path_file = 'XML\_'+ toFile + '.xml'
    root = ElementTree.parse(path_file).getroot()
    c = ElementTree.Element('OCR')
    c.text = words
    root.insert(0, c)
    tree = ElementTree.ElementTree(indent(root))
    tree.write(path_file, xml_declaration=True, encoding='utf-8')

def saveToXmlList(orderList):
    path_file = 'XML\_ocr.xml'
    root = ElementTree.parse(path_file).getroot()
    
    c = ElementTree.Element('Order')
    
   
    customer = ElementTree.SubElement(c, 'Customer')
    customer.text = str(orderList[1]) 
    c.set('nr',customer.text)
           
       
    orderTime = ElementTree.SubElement(c, 'Time')
    orderTime.text = str(orderList[0]) 
        
    for b in orderList[2]:
        
        x = []   
        x.append(b[:1])
        x.append(b[2:])
    
        productOrder = ElementTree.SubElement(c,'ProductOrder')
    
    
        product = ElementTree.SubElement(productOrder,'Quality')
        product.text = str(x[0][0])
        product = ElementTree.SubElement(productOrder,'Product')
        product.text = x[1].lstrip()
        productOrder.set('orderId',customer.text +' '+ product.text )
        productOrder.set('Status','Waiting' )
        productOrder.set('amount', str(x[0][0]))
        
    
    root.insert(0, c)
    tree = ElementTree.ElementTree(indent(root))
    tree.write(path_file, xml_declaration=True, encoding='utf-8')

def saveToXmlFromEmail(orderList):
    path_file = 'XML\_ocr.xml'
    root = ElementTree.parse(path_file).getroot()
    
    c = ElementTree.Element('Order')
    
   
    customer = ElementTree.SubElement(c, 'Customer')
    customer.text = str(orderList[0]) 
    c.set('nr',customer.text)
           
       
    orderTime = ElementTree.SubElement(c, 'Time')
    orderTime.text = orderList[1] 
        

    x = []   
    x.append(orderList[2][:1])
    x.append(orderList[2][2:])
    
    productOrder = ElementTree.SubElement(c,'ProductOrder')
    
    
    product = ElementTree.SubElement(productOrder,'Quality')
    product.text = str(x[0][0])
    product = ElementTree.SubElement(productOrder,'Product')
    product.text = x[1].lstrip()
    productOrder.set('orderId',customer.text +' '+ product.text )
    productOrder.set('Status','Waiting' )
    productOrder.set('amount', str(x[0][0]))
        
    
    root.insert(0, c)
    tree = ElementTree.ElementTree(indent(root))
    tree.write(path_file, xml_declaration=True, encoding='utf-8')

def readOrderXml(toFile):
    path_file = 'XML\_'+ toFile + '.xml'
    tree = ElementTree.parse(path_file)
    root = tree.getroot()
    
    dataList = []

    for order in root.findall('Order'):
        
        dataList.append(buildOrder(order))
    
    return dataList
    
def readXml(toFile):
    path_file = 'XML\_'+ toFile + '.xml'
    tree = ElementTree.parse(path_file)
    root = tree.getroot()
    data = []
    for elem in root.iter('OCR'):
        data.append(elem.text) 
      
    return data   

def changeStatusOnOrderXml(toFile, orderFind,status ,amount):
    path_file = 'XML\_'+ toFile + '.xml'
    tree = ElementTree.parse(path_file)
    root = tree.getroot()
    orders = root.findall('.//ProductOrder')
    listForSave = []
    for order in orders:
        value = order.get('orderId')    
        if(orderFind == value ):
            
            #amountOfPrints = int(order.get('amount'))
            #cala = int(amount)-amountOfPrints
            #order.set('amount',cala)
            
            #if(cala == 0):
                
            order.set('Status',status)

    tree = ElementTree.ElementTree(indent(root))
    tree.write(path_file, xml_declaration=True, encoding='utf-8')

def findOrderXml(toFile, orderFind):
    path_file = 'XML\_'+ toFile + '.xml'
    tree = ElementTree.parse(path_file)
    root = tree.getroot()

    for order in root.findall('Order'):
        value = order.get('nr')
        if(orderFind == value ):
          data = buildOrder(order)

    return data
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
    orderTime = order.find('Time').text
    status = order.findall('ProductOrder')

    for productOrder in status:
        status = productOrder.get('Status')      
        quality = productOrder.get('amount')    
        productText = productOrder[1].text
        data.append(status)
        data.append(customer)
        data.append(orderTime)
        data.append(quality)
        data.append(productText)
        
        
    return data
