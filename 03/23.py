#coding:utf-8
import re

# 正規表現 '=='で挟まれている文字列を想定
comp = re.compile(r'={2,}[\w]+={2,}')
with open('United_Kingdom.txt','r') as f:
    for line in f.readlines():
        section = comp.search(line)
        # 正規表現にマッチするなら
        if section:
            text = section.group(0)
            # '='の数でレベルを判断
            print ('name:%s\tlevel:%d'%(text.replace('=',''),text.count('=')/2-1))

"""
$ python 23.py
name:国名       level:1
name:歴史       level:1
name:地理       level:1
name:気候       level:2
name:政治       level:1
name:外交と軍事 level:1
name:地方行政区分       level:1
name:主要都市   level:2
name:科学技術   level:1
name:経済       level:1
name:鉱業       level:2
name:農業       level:2
name:貿易       level:2
name:通貨       level:2
name:企業       level:2
name:交通       level:1
name:道路       level:2
name:鉄道       level:2
name:海運       level:2
name:航空       level:2
name:通信       level:1
name:国民       level:1
name:言語       level:2
name:宗教       level:2
name:教育       level:2
name:文化       level:1
name:食文化     level:2
name:文学       level:2
name:音楽       level:2
name:イギリスのポピュラー音楽   level:3
name:映画       level:2
name:コメディ   level:2
name:国花       level:2
name:世界遺産   level:2
name:祝祭日     level:2
name:スポーツ   level:1
name:サッカー   level:2
name:競馬       level:2
name:モータースポーツ   level:2
name:脚注       level:1
name:関連項目   level:1
name:外部リンク level:1
"""
