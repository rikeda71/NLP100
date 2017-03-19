#config:utf-8
import re

with open('United_Kingdom.txt','r') as f:
    for line in f.readlines():
        # Categoryが見つかったら
        if line.find('Category') > -1:
            #文頭からとカテゴリ名以外から文字を消す
            a = re.sub(r'[|*\]]+[\w]*','',line.replace('[[Category:',''))
            print(a,end='')

"""
$ python 22.py
イギリス
英連邦王国
G8加盟国
欧州連合加盟国
海洋国家
君主国
島国
1801年に設立された州・地域
"""
