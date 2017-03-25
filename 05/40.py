#coding:utf-8
from morph import Morph

def main():
    # 結果の格納用
    morph_list = []
    i = 0
    with open('neko.txt.cabocha','r') as f:
        for line in f.readlines():
            # 係り受け解析による区切りなら
            if line.find('*') == 0:
                # 文節の開始地点なら
                if int(line[2]) == 0:
                    # listの中にリストを追加
                    morph_list.append(list())
                    # 次のリストの位置を保持
                    i += 1
            # 文章の一部で条件を満たしているなら
            #elif line.find('EOS') == -1 and line[0] != '　':
            elif line.find('EOS') == -1:
                # 品詞情報を格納
                speech = line[line.find('\t')+1:].replace('\n','').split(',')
                # 形態素のクラスを現在の文章を指す配列に挿入
                morph = Morph(line[0:line.find('\t')], speech[6], speech[0], speech[1])
                morph_list[i-1].append(morph)
    
    # 3行目を出力
    for i in range(len(morph_list[2])):
        morph_list[2][i].show()

if __name__ == '__main__':
    main()
