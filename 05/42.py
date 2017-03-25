#coding:utf-8
import re
from morph import Morph
from chunk import Chunk

def read_chunks(filename='') -> list:
    chunks_list = [] # 結果の格納用
    chunks = [] # 1文の解析結果を格納
    chunk = None # 文節

    with open(filename,'r',encoding='utf-8') as f:
        for line in f.readlines():
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
                    chunks_list.append(chunks)
                # リセット
                chunk = None
                chunks = []
            else:
                # 形態素の情報を文節に格納
                speech = line[line.find('\t')+1:].replace('\n','').split(',')
                morph = Morph(line[0:line.find('\t')], speech[6], speech[0], speech[1])
                chunk.morphs.append(morph)

    return chunks_list

if __name__ == '__main__':
    sentences = read_chunks('neko.txt.cabocha')
    print_line = ''
    for i in range(len(sentences[7])):
        print_line += sentences[7][i].paragraphs_str()
        for j in sentences[7][i].srcs:
            if j > -1:
                print_line += '\t'+sentences[7][j].paragraphs_str()
        print_line += '\n'
    print_line = re.sub(r'[!-~]','',print_line) # 半角記号削除
    print_line = re.sub(r'[︰-＠、。]','',print_line) # 全角記号削除
    print(print_line)
