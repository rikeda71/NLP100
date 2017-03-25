#coding:utf-8
import re

class Morph:
    surface = '' # 表層系
    base = '' # 基本形
    pos = '' # 品詞
    pos1 = '' # 品詞細分類1

    # コンストラクタ
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    # 表示メソッド
    def show(self):
        print('表層系:%s 基本形:%s 品詞: %s 品詞細分類: %s'%(self.surface, self.base, self.pos, self.pos1))

class Chunk:
    #morphs # Morphオブジェクトのリスト
    #dst    # 係り先文節インデックス番号
    #srcs   # 係り受け元文節インデックス番号のリスト

    # コンストラクタ
    def __init__(self, morphs, dst, srcs):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs

    # 文字列を返す
    def __str__(self) -> str:
        sentence = ''
        for i in range(len(self.morphs)):
            sentence = sentence + self.morphs[i].surface
        return sentence + '\t係り先:' + str(self.dst)


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
    
    for i in range(len(sentences[7])):
        print(str(i+1)+':'+str(sentences[7][i]))
    
