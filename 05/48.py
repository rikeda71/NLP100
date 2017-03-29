#coding:utf-8
import re
import readfile

# 再帰で名詞から根へのパスを出力するメソッド
def out_pass_end(chunk,i) -> str:
    if chunk[i].dst == -1:
        return chunk[i].paragraphs_str() + '\n'
    else:
        return chunk[i].paragraphs_str() + '->' + out_pass_end(chunk,chunk[i].dst)

if __name__ == '__main__':
    sentences = readfile.read_chunks('neko.txt.cabocha')
    out_line = ''
    dis = [] # 助詞の位置
    for i in range(len(sentences)):
        for j in range(len(sentences[i])):
            # 名詞から始まるならパスを追加
            if sentences[i][j].bool_in_speech('名詞'):
                out_line += out_pass_end(sentences[i],j) 

    with open('out48.txt','w') as f:
        f.write(out_line)
