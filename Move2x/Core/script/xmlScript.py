from xml.dom import minidom
from xml.etree import ElementTree
import os 

def createXml(dateFrom,toFile,main):
    root = minidom.Document()

    xml = root.createElement('root')
    root.appendChild(xml)

    productChild = root.createElement(dateFrom)
    listOfFile = []
    
    if isinstance(toFile, str):
        listOfFile.append(toFile)
        print(isinstance(toFile, str))
    elif isinstance(toFile, str):
        listOfFile = toFile
        print(isinstance(toFile, str))
    
    xml_str = root.toprettyxml(indent = "\t")
    path_file = ''
    for item in listOfFile:
        if(main == 'main'):
            path_file = 'script\_'+ item + '.xml'
        else:
            path_file ='_' + item + '.xml'

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
    listOfFile = []
    
    if isinstance(toFile, str):
        listOfFile.append(toFile)
        print(isinstance(toFile, str))
    elif isinstance(toFile, str):
        listOfFile = toFile
        print(isinstance(toFile, str))
    
    xml_str = root.toprettyxml(indent = "\t")
    path_file = ''
    for item in listOfFile:
        if(main == 'main'):
            path_file = 'script\_'+ item + '.xml'
        else:
            path_file ='_' + item + '.xml'
    root = ElementTree.parse(path_file).getroot()
    c = ElementTree.Element(dateFrom)
    c.text = words
 
    root.insert(1, c)
    tree = ElementTree.ElementTree(indent(root))
    tree.write(path_file, xml_declaration=True, encoding='utf-8')

def readXml(toFile, main):
    path_file = ''
    if(main == 'main'):
        path_file = 'script\_'+ toFile + '.xml'
    else:
        path_file ='_' + toFile + '.xml'

    tree = ElementTree.parse(path_file)
    root = tree.getroot()
    data = []
    for elem in root:
        data.append(elem.text) 
   
    return data
    
   
