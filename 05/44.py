#coding:utf-8
import re
import CaboCha
import pydot_ng
from morph import Morph
from chunk import Chunk

def cabocha_parse(sentence) -> str:
    c = CaboCha.Parser()
    tree = c.parse(sentence)
    return tree.toString(CaboCha.FORMAT_LATTICE)


def read_chunks(sentence) -> list:
    chunks = [] # 1文の解析結果を格納
    chunk = None # 文節

    for line in sentence.splitlines():
        # 係り受け解析による区切りなら
        if line.find('*') == 0:
            # 係り先が書かれている位置
            dep_par = re.search('[-]*[0-9]+D',line).start()
            if chunk is not None:
                chunks.append(chunk)
            chunk = Chunk( [], int(line[dep_par:line.find('D')]), [] )
        # 1文の終了の記号が見つかれば
        elif line.find('EOS') > -1:
            if chunk is not None:
                chunks.append(chunk)
            if len(chunks) > 0:
                # 係り受け元の格納
                for i in range( len(chunks) ):
                    if chunks[i].dst > -1:
                        chunks[chunks[i].dst].srcs.append(i)
                # 1文を格納
                return chunks
        else:
            # 形態素の情報を文節に格納
            speech = line[line.find('\t')+1:].replace('\n','').split(',')
            morph = Morph(line[0:line.find('\t')], speech[6], speech[0], speech[1])
            chunk.morphs.append(morph)

    return chunks_list

if __name__ == '__main__':
    sentence = input()
    cabocha_tree = cabocha_parse(sentence)
    chunks = read_chunks(cabocha_tree)
    edges = []
    for i in range(len(chunks)):
        if chunks[i].dst > -1:
            edges.append([chunks[i].paragraphs_str(), chunks[chunks[i].dst].paragraphs_str()])
    print(edges)
    g = pydot_ng.graph_from_edges(edges)
    g.write_jpeg('chunk_info_graph.jpg',prog='dot')
