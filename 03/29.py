#coding:utf-8
import re
import urllib.request
import json

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

# urlを作成してjsonファイルを取得してくる
url = 'https://ja.wikipedia.org/w/api.php?action=query&format=json&prop=imageinfo&iiprop=url&titles=File:'+urllib.parse.quote(dic['国旗画像'],'utf-8')
res = urllib.request.urlopen(url)
jsonData = res.read()
# jsonファイルを辞書型に格納し、urlの情報だけを出力
dic = json.loads(jsonData)
print(dic['query']['pages']['-1']['imageinfo'][0]['url'])

"""
$ python 29.py
https://upload.wikimedia.org/wikipedia/commons/a/ae/Flag_of_the_United_Kingdom.svg
"""
