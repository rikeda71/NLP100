import xml.etree.ElementTree as ET
import corenlp

if __name__ == '__main__':
    tree = ET.parse('nlp.txt.xml')
    root = tree.getroot()
    for tree in root[0][0][0]:
        for word in tree.iter('word'):
            print(word.text)
