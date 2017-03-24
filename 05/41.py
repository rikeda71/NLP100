#coding:utf-8
import re
import copy

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
    morphs = [] # Morphオブジェクトのリスト
    dst = 0 # 係り先文節インデックス番号
    srcs = [] # 係り受け元文節インデックス番号のリスト

    # コンストラクタ
    def __init__(self, dst):
        self.dst = dst

    # リストに形態素を追加
    def add_morph(self, morph):
        self.morphs.append(morph)

    # 係り受け元文節インデックス番号を追加
    def add_src(self, src):
        self.srcs.append(src)
    
    # 係り先を返す
    def get_dst(self):
        return self.dst

def main():
    chunks_list = [] # 結果の格納用
    chunks = [] # 1文の解析結果を格納
    i = 0 # 文節の位置

    with open('neko.txt.cabocha','r') as f:
        for line in f.readlines():
            # 係り受け解析による区切りなら
            if line.find('*') == 0:
                # 係り先が書かれている位置
                dep_par = re.search('[-]*[0-9]+D',line).start()
                # 文節の開始地点なら
                if int(line[2]) == 0:
                    # 係り受け元の格納
                    for j in range( len(chunks) ):
                        chunks[chunks[j].get_dst()].add_src(j)
                    # 結果に格納し、1文の結果をリセット
                    if len(chunks) > 0:
                        chunks_list.append(chunks)
                        chunks.clear()
                    i = 0 # 1文の処理が終わったので文節の位置もリセット
                    # 次の文の格納開始
                    chunks.append(Chunk( int( line[dep_par:line.find('D')] ) ))
                # それ以外なら1文の解析結果を追加
                else:
                    chunks.append(Chunk( int( line[dep_par:line.find('D')] ) ))
                    i += 1

            # 文章の一部なら
            elif line.find('EOS') == -1:
                # 品詞情報を格納
                speech = line[line.find('\t')+1:].replace('\n','').split(',')
                # 形態素のクラスを文節に挿入
                morph = Morph(line[0:line.find('\t')], speech[6], speech[0], speech[1])
                chunks[i].add_morph(morph)
    
    # 8行目の文節を出力
    for j in range(len(chunks_list[7])):
        print('係り先:%d    '%(chunks_list[7][j].get_dst()))
        for k in range(len(chunks_list[7][j].morphs)):
            print(k,chunks_list[7][j].morphs[k].surface)

if __name__ == '__main__':
    main()
