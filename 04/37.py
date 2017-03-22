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
val_list = []
label = []
i = 0
# 値で降順ソートして上位10件だけ格納
for k,v in sorted(count_dic.items(),key=lambda x:x[1],reverse=True):
    val_list.append(v)
    label.append(str(k))
    i += 1
    if i==10:
        break

#棒グラフの描画
left = np.array([1,2,3,4,5,6,7,8,9,10])
height = np.array(val_list)
plt.bar(left,height,tick_label = label)
plt.show()
