"""
jsonファイルの各要素をリストに格納するプログラム
ex.) jsonData[0]["title"] だと最初の要素のtitleの値が呼び出される
"""

#config:utf-8
import json
import re

i=0
jsonData = []
# json形式のテキストを1行ごとに分割
with open('jawiki-country.json','r') as f:
    #data = f.readlines()
    for line in f.readlines():
        jsonData.append(dict())
        jsonData[i] = json.loads(line)
        i += 1

print(jsonData[0]["title"])
