#coding:utf-8
import xml.etree.ElementTree as ET
import pydot_ng

# xml->corenlp->pydot
def get_collapsed(filename):
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
        edges = get_sentence(sentence)
        draw_graph(edges,i)

# 1文の参照関係を得る
def get_sentence(sentence) -> list:
    array = []
    for i in range(len(sentence)):
        array.append([sentence[i][0].text,sentence[i][1].text])
    return array

# 得たデータを描画する
def draw_graph(array,i):
    g = pydot_ng.graph_from_edges(array)
    g.write_jpeg('graph/' + str(i) +'.jpg',prog='dot')

if __name__ == '__main__':
    get_collapsed('nlp.txt.xml')
