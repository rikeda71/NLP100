#coding:utf-8
import re

# 辞書型の定義
dic = {}
with open('United_Kingdom.txt','r') as f:
    for line in f.readlines():
        # テンプレートの型であれば
        if line.find(' = ') > -1:
            # フィールドと値に分割して辞書に
            text = line[1:].split(' = ')
            # リファレンス(ref)があれば削除する
            if re.search(r'<ref',text[1]):
                text[1] = text[1][:(re.search(r'<ref',text[1])).start()]
            # 内部リンクにマッチしているかどうか
            match = re.search(r'\[{2}.*?(#|\||\]{2})',text[1])
            # 内部リンクの削除
            if match:
                dic[text[0]] = re.sub(r'(#|\||\])','',text[1][match.start()+2:match.end()])
            else: 
                dic[text[0]] = re.sub(r'\'{2,5}','',text[1].replace('\n',''))

print('\n'.join(k+':'+v for k, v in dic.items()))
