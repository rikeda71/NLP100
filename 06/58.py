#coding:utf-8
import xml.etree.ElementTree as ET
import pydot_ng

# xml->corenlp->係り受け解析結果
def puts_tuples(filename):
    i = 0
    tree = ET.parse(filename)
    root = tree.getroot()
    for sentence in root.iterfind('./document/sentences/sentence/'):
        # 係り受け解析以外の結果なら
        if not 'type' in sentence.attrib:
            continue
        elif sentence.attrib['type'] != 'collapsed-dependencies':
            continue
        i += 1
        get_dependencies(sentence)

# 1文の参照関係を得る
def get_dependencies(sentence):
    """
    ex)
    num_dict {0:ROOT, 1:word, ...}
    dependencies {ROOT:{'nsubj':[1,4],'dobj':[3,6]}, word: ...}
    """
    num_dict = {} # インデックスと単語の関係を保持
    dependencies = {} # 係り受け情報を格納
    for i in range(len(sentence)):
        dep = sentence[i]
        # 係り受け情報に含まれないなら新しく作る
        if not dep[0].text in dependencies:
            dependencies[dep[0].text] = {'nsubj':[], 'dobj':[]}
        # 単語情報を格納していないなら格納する
        if not dep[0].attrib['idx'] in num_dict:
            num_dict[dep[0].attrib['idx']] = dep[0].text
        if not dep[1].attrib['idx'] in num_dict:
            num_dict[dep[1].attrib['idx']] = dep[1].text
        # ほしい情報なら格納
        if dep.attrib['type'] in 'nsubj':
            dependencies[dep[0].text]['nsubj'].append(dep[1].attrib['idx'])
        elif dep.attrib['type'] in 'dobj':
            dependencies[dep[0].text]['dobj'].append(dep[1].attrib['idx'])
    show_relation(dependencies,num_dict)

def show_relation(dep, num):
    for k in num.keys():
        if not num[k] in dep:
            continue
        if len(dep[num[k]]['nsubj']) > 0 and len(dep[num[k]]['dobj']) > 0:
            line = ''
            for i in dep[num[k]]['nsubj']:
                line += num[i] + ' '
            line = line[:-1] + '\t' + num[k] +'\t'
            for i in dep[num[k]]['dobj']:
                line +=num[i] + ' '
            print(line[:-1])

if __name__ == '__main__':
    puts_tuples('nlp.txt.xml')
