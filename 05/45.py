#coding:utf-8
import re
import readfile

if __name__ == '__main__':
    sentences = readfile.read_chunks('neko.txt.cabocha')
    out_line = ''
    dis = [] # 助詞の位置
    for i in range(len(sentences)):
        for j in range(len(sentences[i])):
            flag = False
            dis.clear()
            # 動詞なら
            if sentences[i][j].bool_in_speech('動詞'):
                # さらに副詞がかかっているなら
                for k in sentences[i][j].srcs:
                    if sentences[i][k].bool_in_speech('助詞'):
                        flag = True
                        dis.append(k)
                # 条件を満たしていたら
                if flag:
                    # 動詞の追加
                    for k in range(len(sentences[i][j].morphs)):
                        if sentences[i][j].morphs[k].pos in '動詞':
                            out_line = out_line +  sentences[i][j].morphs[k].base + '\t'
                            break
                    # 助詞の追加
                    for k in dis:
                        for l in range(len(sentences[i][k].morphs)):
                            if sentences[i][k].morphs[l].pos in '助詞':
                                out_line = out_line + sentences[i][k].morphs[l].surface + ' '
                    # 改行の追加
                    out_line = out_line + '\n'
    
    with open('out45.txt','w') as f:
        f.write(out_line)


    #print(out_line,end='')
