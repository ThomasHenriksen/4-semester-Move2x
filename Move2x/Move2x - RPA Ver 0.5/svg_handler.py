import xml.sax
import xml.etree.ElementTree as ET
import os 

c = '_ocr'
path_file = 'XML\_'+ c + '.xml'
xmlfile = path_file

tree = ET.parse(xmlfile)
root = tree.getroot()

ET.dump(tree)
for elm in root.findall("."):
    print (elm.tag)


class ProductHandler(object):
    """description of class"""

        

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
        for elem in root:
            data.append(elem.text) 
        print (data)
        return data
  
