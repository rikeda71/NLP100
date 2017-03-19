#config:utf-8
import json
import re

# json形式のテキストを1行ごとに分割
with open('jawiki-country.json','r') as f:
    for line in f.readlines():
        jsonData = json.loads(line)
        # イギリスが出た時点でテキストを保持して終了
        if jsonData['title'] in 'イギリス':
            text = jsonData['text']
            break

# テキストファイルに書き込み
f = open('United_Kingdom.txt','w')
f.write(text)
f.close()
