import xml.etree.ElementTree as et
menuFile = "8.DataHasToGoSomewhere/xml_files/menu.xml"
tree = et.ElementTree(file=menuFile)
root = tree.getroot()
print(root.tag)

for child in root:
    print('tag:',child.tag,'attributes:',child.attrib)
    for grandchild in child:
        print('\ttag:',grandchild.tag,'attributes:',grandchild.attrib)