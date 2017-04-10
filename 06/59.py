import xml.etree.ElementTree as ET
import re

def show_NP(parse):
    while True:
        dis = parse.find('(NP')
        if dis > -1:
            text = re.split(r'[(][A-Z]+',cut_text(parse[dis:]))
            delete_word(text,'')
            delete_word(text,' ')
            for i in range(len(text)):
                if not re.search('\w',text[i]) == 'None':
                    print(re.sub('[\s|(|)]','',text[i]),end=' ')
            print('')
            parse = parse[dis+3:]
        else:
            break

def delete_word(array:list,word):
    while True:
        if not word in array:
            break
        array.remove(word)

# カッコの数が均等になるまでテキストを切り取る
def cut_text(text):
    new_text = ''
    brackets = 0 # ()の数
    for i in range(len(text)):
        if text[i] == '(':
            brackets+=1
        elif text[i] == ')':
            brackets-=1
        new_text += text[i]
        if brackets <= 0:
            return new_text


if __name__ == '__main__':
    tree = ET.parse('nlp.txt.xml')
    root = tree.getroot()
    for token in root.iter('parse'):
        show_NP(token.text)
