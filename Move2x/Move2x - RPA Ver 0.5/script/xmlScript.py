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

def saveToXml(dateFrom,toFile,words):
    path_file = 'XML\_'+ toFile + '.xml'
    root = ElementTree.parse(path_file).getroot()
    c = ElementTree.Element(dateFrom)
    c.text = words
    test = ElementTree.SubElement(c,'test')
    test.text = 'test'
    root.insert(0, c)
    tree = ElementTree.ElementTree(indent(root))
    tree.write(path_file, xml_declaration=True, encoding='utf-8')

def saveToXmlList(orderList):
    path_file = 'XML\_ocr.xml'
    root = ElementTree.parse(path_file).getroot()
    c = ElementTree.Element('Order')
    for word in orderList:   
        if(isinstance(word, int)):
            customer = ElementTree.SubElement(c, 'Customer')
            customer.text = str(word) 
            c.set('nr',customer.text)
        elif(word[2] == ':'):
            orderTime = ElementTree.SubElement(c, 'Time')
            orderTime.text = word 
        else:
            x = []
            try:
                 x = order.split('.')
            except:
                 x.append(word[:5])
                 x.append(word[5:])
                 product = ElementTree.SubElement(c,'Quality')
                 product.text = str(x[0][0])
                 product = ElementTree.SubElement(c,'Product')
                 product.text = x[1].lstrip()
        
    
    root.insert(0, c)
    tree = ElementTree.ElementTree(indent(root))
    tree.write(path_file, xml_declaration=True, encoding='utf-8')

def readOrderXml(toFile):
    path_file = 'XML\_'+ toFile + '.xml'
    tree = ElementTree.parse(path_file)
    root = tree.getroot()
    
    dataList = []

    for order in root.findall('Order'):
        data = []
        customer = order.find('Customer').text
        orderTime = order.find('Time').text
        
        qualitys = order.findall('Quality')
        products = order.findall('Product')
        listProducts = []
        i = 0
        for product in products:
            quality = qualitys[i].text
            productText = product.text
            listProducts.append(quality)
            listProducts.append(productText)
            i += 1
        data.append(customer)
        data.append(orderTime)
        data.append(listProducts)
        dataList.append(data)
    return dataList
    
def readXml(toFile):
    path_file = 'XML\_'+ toFile + '.xml'
    tree = ElementTree.parse(path_file)
    root = tree.getroot()
    data = []
    for elem in root.iter():
        data.append(elem.text) 
   
    return data   

def deleteOrderXml(toFile, Order):
    path_file = 'XML\_'+ toFile + '.xml'
    tree = ElementTree.parse(path_file)
    root = tree.getroot()
    
    

    for order in root.findall('Order'):
        value = order.get('nr')
        if(Order == value):
           root.remove(order)
    
    ElementTree.dump(root)
    #return dataList