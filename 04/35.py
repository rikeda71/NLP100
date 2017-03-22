#coding:utf-8
import MeCab
import re
import queue

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
# キュー
q = queue.Queue()
for j in range(len(dic)):
    # 名詞ならキューにつっこむ
    if dic[j]['pos'] in '名詞':
        q.put(dic[j]['surface'])
    # 名詞ではないならキューを全て吐き出す
    elif not q.empty():
        while not q.empty():
            print(q.get(),end="")
        print("")
