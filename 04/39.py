#coding:utf-8
import MeCab
import re
import numpy as np
import matplotlib.pyplot as plt

# リスト
dic = {}
tagger = MeCab.Tagger()
i=0

with open('neko.txt','r') as f:
    for line in f.readlines():
        # リストの中に辞書を追加
        result = tagger.parseToNode(line)
        # 分かち書きごとに
        while result:
            # 最初と最後の文字は無視
            if result.surface in 'BOS/EOS':
                pass
            # まだ辞書の中に格納されていないなら
            else:
                split = (result.feature).split(',')
                dic[i] = {'surface':result.surface,
                               'base':split[6],
                               'pos':split[0],
                               'pos1':split[1]}
                i += 1
            # 次のテキストに移動
            result = result.next

# 数をカウントする辞書
count_dic = {}
for i in range(len(dic)):
    # 半角スペースはスルー
    if dic[i]['surface'] in '\u3000':
        pass
    # 存在するならカウント
    elif str(dic[i]['surface']) in count_dic:
        count_dic[str(dic[i]['surface'])] = count_dic[str(dic[i]['surface'])] + 1
    # 存在しないなら追加
    else:
        count_dic[str(dic[i]['surface'])] = 1

# プロット用
val_array = []
log_rank = []
i = 1

# 値で降順ソートして出力
for k,v in sorted(count_dic.items(),key=lambda x:x[1],reverse=True):
    # リストにない値なら追加
    if v not in val_array:
        val_array.append(np.log(v))
        log_rank.append(np.log(i))
        i += 1

plt.scatter(log_rank,val_array)
plt.show()
