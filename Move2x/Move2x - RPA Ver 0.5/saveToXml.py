import xml.dom.minidom
import xml.etree.ElementTree as ET
from xml.sax import parse
import os 

class XmlScript(object):
    """description of class"""

    ## groupe = root  tag =  productChild = root.createElement(dateFrom)
    

     
    def saveToXml(dateFrom,toFile,words, main):
        path_file = ''
        if(main == 'main'):
           path_file = 'XML\_'+ toFile + '.xml'
        else:
           path_file ='_' + toFile + '.xml'

        root = ElementTree.parse(path_file).getroot()
        c = ElementTree.Element(dateFrom)
        c.text = words
 
        root.insert(1, c)
        tree = ElementTree.ElementTree(indent(root))
        tree.write(path_file, xml_declaration=True, encoding='utf-8')

   


