import xml.etree.ElementTree as ET
import corenlp

if __name__ == '__main__':
    tree = ET.parse('nlp.txt.xml')
    root = tree.getroot()
    for word in root.iter('word'):
        print(word.text)
