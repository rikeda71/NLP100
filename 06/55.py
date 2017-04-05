import xml.etree.ElementTree as ET

if __name__ == '__main__':
    tree = ET.parse('nlp.txt.xml')
    root = tree.getroot()
    for token in root.iter('token'):
      if token[5].text == 'PERSON':
          print(token[0].text)
