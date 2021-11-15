from xml.dom import minidom
from xml.etree import ElementTree
import os 

def createXml(toFile):
    root = minidom.Document()
    xml = root.createElement('root')
    root.appendChild(xml)
    #productChild = root.createElement(dateFrom)
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

def saveToXml(dateFrom,toFile,words, main):
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
    path_file = 'XML\_ocr2.xml'
    root = ElementTree.parse(path_file).getroot()
    c = ElementTree.Element('Order')
    for word in orderList:
        if(isinstance(word, int)):
            customer = ElementTree.SubElement(c, 'Customer')
            customer.text = str(word) 
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
def readXml(toFile):
    path_file = ''
    main = 'main'
    if(main == 'main'):
        path_file = 'XML\_'+ toFile + '.xml'
    else:
        path_file ='_' + toFile + '.xml'

    tree = ElementTree.parse(path_file)
    root = tree.getroot()
    data = []
    for elem in root.iter():
        data.append(elem.text) 
   
    return data
    
   
