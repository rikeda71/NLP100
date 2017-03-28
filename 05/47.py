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
    out_line = ''
    dis = [] # 助詞の位置
    for i in range(len(sentences)):
        for j in range(len(sentences[i])):
            flag = False
            dis.clear()
            # 「サ変+を+動詞」なら
            if sentences[i][j].bool_in_speech('動詞'):
                for k in sentences[i][j].srcs:
                    if sentences[i][k].bool_in_speech_detaile('サ変接続')\
                        and sentences[i][k].morph_in_str('を'):
                            flag = True
                            sahen = k
                            chunk = sentences[i][k]
                if not flag:
                    break
                flag = False
                # さらに助詞がかかっているなら
                for k in sentences[i][j].srcs:
                    if sentences[i][k].bool_in_speech('助詞'):
                        flag = True
                        dis.append(k)
                # 条件を満たしていたら
                if flag:
                    out_line = out_line + chunk.paragraphs_str()
                    for k in range(len(sentences[i][chunk.dst].morphs)):
                        if sentences[i][chunk.dst].morphs[k].pos == '動詞':
                            out_line = out_line + sentences[i][chunk.dst].morphs[k].base + '\t'
                            break
                    # 助詞の追加
                    for k in dis:
                        for l in range(len(sentences[i][k].morphs)):
                            if sentences[i][k].morphs[l].pos in '助詞':
                                out_line = out_line + sentences[i][k].morphs[l].surface + ' '
                    # 最後のスペースを消しtabを追加
                    out_line = out_line[:-1] + '\t'
                    # 動詞にかかっている文節を追加
                    for k in sentences[i][j].srcs:
                        out_line = out_line + sentences[i][k].paragraphs_str() + ' '
                    # 改行の追加
                    out_line = out_line + '\n'

    with open('out47.txt','w') as f:
        f.write(out_line)
