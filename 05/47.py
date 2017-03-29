#coding:utf-8
import re
import readfile

if __name__ == '__main__':
    #sentences = read_chunks('neko.txt.cabocha')
    sentences = readfile.read_chunks('neko.txt.cabocha')
    out_line = ''
    dis = [] # 助詞の位置
    for i in range(len(sentences)):
        for j in range(len(sentences[i])):
            verb = False # 動詞
            adverb = False # 副詞
            sahen = -1 # サ変接続名詞の位置
            dis.clear()
            # 「サ変+を+動詞」なら
            if sentences[i][j].bool_in_speech('動詞'):
                for k in sentences[i][j].srcs:
                    if sentences[i][k].bool_in_speech_detaile('サ変接続')\
                        and sentences[i][k].morph_in_str('を'):
                            verb = True
                            sahen = k
                            chunk = sentences[i][k]
                            break
                # さらに助詞がかかっているなら
                for k in sentences[i][j].srcs:
                    if sentences[i][k].bool_in_speech('助詞') and sahen != k:
                        adverb = True
                        dis.append(k)
                # 条件を満たしていたら
                if verb and adverb:
                    out_line = out_line + chunk.paragraphs_str()
                    for k in range(len(sentences[i][chunk.dst].morphs)):
                        if sentences[i][chunk.dst].morphs[k].pos == '動詞' and sahen != k:
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
                        if k != sahen:
                            pass
                            out_line = out_line + sentences[i][k].paragraphs_str() + ' '
                    # 改行の追加
                    out_line = out_line + '\n'

    out_line = re.sub(r'[!-~]','',out_line) # 半角記号削除
    out_line = re.sub(r'[︰-＠、。]','',out_line) # 全角記号削除
    with open('out47.txt','w') as f:
        f.write(out_line)
