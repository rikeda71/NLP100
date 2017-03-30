#coding:utf-8
import re
import readfile

def one_n_to_n(chunk,i,noun) -> str:
    for j in range(i,len(chunk)):
        line += noun
        if chunk[i].dst == j+1
            line += '->'
        else:
            line += '|'
        for k in range(j+1,len(chunk[j])):
            line += chunk[j].morphs[k]


#名詞間への係り受けパスを出力するメソッド
def out_n_to_n(chunk) -> str:
    noun = ''
    lines = []
    for j in range(len(chunk)):
        # 名詞がないなら無視する
        # 一番端でも無視する
        if not chunk[j].bool_in_speech('名詞')\
                or j+1 == len(chunk):
            continue
        # X の名詞文字列を作成
        for k in range(len(chunk[j].morphs)):
            if chunk[j].morphs[k].pos in '名詞':
                noun += noun + 'X'
            else:
                noun += chunk[j].morphs[k].surface
        # Y以降の文字列を作成
        lines.append(one_n_to_n(chunk,j+1,noun))
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
            if chunk[j].dst == j+1:
                line += '->'
            else:
                line += '|'
                """
                まだ、ｘで初めてｙとｘで初めて人間というｙについての対応ができていない
                違いは、｜がない場合に、XとYが揃えばそく終了というところ？？
                どう区別するかが難しいorz
                """
            lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    sentences = readfile.read_chunks('neko.txt.cabocha')
    out_line = ''
    dis = [] # 助詞の位置
    for i in range(len(sentences)):
                out_line += out_n_to_n(sentences[i],j) 

    with open('out49.txt','w') as f:
        f.write(out_line)
