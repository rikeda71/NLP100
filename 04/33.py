#coding:utf-8
import MeCab

# リスト
dic = {}

with open('neko.txt','r') as f:
    tagger = MeCab.Tagger()
    for line in f.readlines():
        # リストの中に辞書を追加
        result = tagger.parseToNode(line)
        # 分かち書きごとに
        while result:
            # まだ辞書の中に格納されていないなら
            if result.surface not in dic:
                split = (result.feature).split(',')
                dic[result.surface] = {'surface':result.surface,
                                       'base':split[6],
                                       'pos':split[0],
                                       'pos1':split[1]}
            # 次のテキストに移動
            result = result.next

"""
サ変接続の名詞とは、後ろに「～される」「～した」などが続いても違和感のない名詞のこと
"""
for k, v in dic.items():
    if v['pos1'] in 'サ変接続':
        print(v['base'])
