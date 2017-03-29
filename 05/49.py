#coding:utf-8
import re
import readfile

#名詞間への係り受けパスを出力するメソッド
def out_n_to_n(chunk,i) -> str:
    # X の名詞文字列を作成
    noun = ''
    for j in range(len(chunk[i].morphs)):
        if chunk[i].morphs[j].pos in '名詞':
            noun += noun + 'X'
        else:
            noun += chunk[i].morphs[j].surface
    # Y以降の文字列を作成
    lines = []
    # ペアを探す
    for j in range(i,len(chunk)):
        line = noun
        noun_flag = False
        # 1つの組み合わせを作る
        for k in range(len(chunk[j].morphs)):
            if chunk[j].morphs[k].pos in '名詞' and not noun_flag:
                noun_flag = True
                line += 'Y'
            else:
                line += chunk[j].morphs[k].surface
            # 構文木の経路上かどうか
            if chunk[j].morphs[k].dst == j+1
                line += '->'
            else:
                line += '|'
                """
                まだ、ｘで初めてｙとｘで初めて人間というｙについての対応ができていない
                違いは、｜がない場合に、XとYが揃えばそく終了というところ？？
                どう区別するかが難しいorz
                """
        lines.append(line)

if __name__ == '__main__':
    sentences = readfile.read_chunks('neko.txt.cabocha')
    out_line = ''
    dis = [] # 助詞の位置
    for i in range(len(sentences)):
        for j in range(len(sentences[i])):
            # 名詞から始まるならパスを追加
            if sentences[i][j].bool_in_speech('名詞'):
                out_line += out_n_to_n(sentences[i],j) 

    with open('out49.txt','w') as f:
        f.write(out_line)
