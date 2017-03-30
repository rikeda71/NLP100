#coding:utf-8
import re
import readfile

# 名詞句ペアの係り受けパスを出力
def one_n_to_n(chunk, x, y) -> str:
    line = ''
    # 2つの名詞句の地点まで構文木を追っていく
    for i in range(x,y+1):
        # 参照文節に名詞句が含まれるなら
        if chunk[i].bool_in_speech('名詞'):
            if i == x:
                line += chunk[i].paragraphs_mask_str('X','名詞')
            # 名詞句ペアが構文木上にあったので探索終了
            elif i == y:
                line += chunk[i].paragraphs_mask_str('Y','名詞',True)
                return line
            else:
                line += chunk[i].paragraphs_str()
        # 含まれないならマスク(X,Yへの置換)を考慮しない
        else:
            line += chunk[i].paragraphs_str()

        # 次の文節に今の文節がなら
        if chunk[i].dst == i+1:
            line += '->'
        # そうじゃないなら
        else:
            # xの目指すべきところを保持
            x_dst = chunk[i].dst
            # 分岐して参照する名詞句までワープ
            line += '|'
            line += chunk[y].paragraphs_mask_str('Y','名詞')
            if chunk[y].dst == x_dst:
                line += '|' + chunk[x_dst].paragraphs_str()
                return line
            elif chunk[y].dst == y+1:
                line += '->'
            else:
                line += '|'
            break

    # それ以外なら交わるまで続く
    for i in range(y+1,len(chunk)):
        line += chunk[i].paragraphs_str()
        # 終了
        if i == x_dst:
            return line + chunk[i].paragraphs_str()
        # 次に指す位置でxと合流するなら終了
        elif chunk[i].dst == x_dst:
            line += '|' + chunk[x_dst].paragraphs_str()
            return line
        # それ以外なら
        # 次の文節に今の文節が係るなら
        elif chunk[i].dst == i+1:
            line += '->'
        # 違うなら分岐
        else:
            line += '|'
    """
    共通の地点で交わらない場合は無視
    ex.)yがゴールでその経路途中を飛ばしてしまうときなど
    """
    return ''

#すべての名詞ペアの係り受けパスを出力するメソッド
def out_n_to_n(chunk) -> str:
    lines = [] # 文字列
    noun_list = [] # 名詞の存在する位置の保存
    for i in range(len(chunk)):
        if chunk[i].bool_in_speech('名詞'):
            noun_list.append(i)
    # 名詞句が2つ未満なら終了
    if len(noun_list) <= 1:
        return ''
    # 名詞句のすべての組み合わせのループ
    for i in range(len(noun_list)):
        for j in range(i+1,len(noun_list)):
            lines.append(one_n_to_n(chunk, noun_list[i], noun_list[j]))
    # 空行を削除
    while lines.count('') > 0:
        lines.remove('')
    return '\n'.join(lines)

if __name__ == '__main__':
    sentences = readfile.read_chunks('neko.txt.cabocha')
    out_line = ''
    # 各文の係り受けパスを取得
    for i in range(len(sentences)):
        out_line += out_n_to_n(sentences[i]) + '\n'

    with open('out49.txt','w') as f:
        f.write(out_line)
