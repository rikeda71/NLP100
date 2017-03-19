#config:utf-8

with open('United_Kingdom.txt','r') as f:
    for line in f.readlines():
        # Categoryが見つかったら出力
        if line.find('Category') > -1:
            print(line,end="")

"""
$ python 21.py
[[Category:イギリス|*]]
[[Category:英連邦王国|*]]
[[Category:G8加盟国]]
[[Category:欧州連合加盟国]]
[[Category:海洋国家]]
[[Category:君主国]]
[[Category:島国|くれいとふりてん]]
[[Category:1801年に設立された州・地域]]
"""
