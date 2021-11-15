import xml.etree.ElementTree as ET
from xml.dom import minidom


# Create root element.
root = ET.Element("root")
 
# Add sub element.
country = ET.SubElement(root, "country", name="Canada")
 
# Add sub-sub element.
quebec = ET.SubElement(country, "province")
quebec.text = "Quebec"
 
ontario = ET.SubElement(country, "province")
ontario.text = "Ontario"
ontario.set("rank", "2")    # Set attribute rank="2"
 
# One-liner to create Alberta province.
ET.SubElement(country, "province", rank="3", category="oil").text = "Alberta"
 
# Write XML file.
tree = ET.ElementTree(root)
tree.write("canada.xml")


xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
with open("canada-pretty.xml", "w") as f:
    f.write(xmlstr)


