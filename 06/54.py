import xml.etree.ElementTree as ET

if __name__ == '__main__':
    tree = ET.parse('nlp.txt.xml')
    root = tree.getroot()
    for token in root.iter('token'):
        print('%s\t%s\t%s'%(token[0].text,token[1].text,token[4].text))
