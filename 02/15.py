#config:utf-8
import sys
import linecache

# コマンドライン引数を受け取る
# 無かったら10行(headコマンドと同様)
argvs = sys.argv
if len(argvs) <= 1:
    row = 10
else:
    row = int(argvs[1])

# とりあえず全テキストを保持
lines = []
for line in open('hightemp.txt','r'):
    lines.append(line)

# 引数が行数より大きいときとそうでないときで分岐
val = len(lines) - row
if val <= 0:
    print(''.join(lines),end="")
else:
    text = ''
    for i in range(val,len(lines)):
        text = text + lines[i]
    print(text,end="")

"""
$ sdiff -w80 <(tail -n8 hightemp.txt) <(python 15.py 8)
岐阜県  美濃    40      2007-08-16      岐阜県  美濃    40      2007-08-16
群馬県  前橋    40      2001-07-24      群馬県  前橋    40      2001-07-24
千葉県  茂原    39.9    2013-08-11      千葉県  茂原    39.9    2013-08-11
埼玉県  鳩山    39.9    1997-07-05      埼玉県  鳩山    39.9    1997-07-05
大阪府  豊中    39.9    1994-08-08      大阪府  豊中    39.9    1994-08-08
山梨県  大月    39.9    1990-07-19      山梨県  大月    39.9    1990-07-19
山形県  鶴岡    39.9    1978-08-03      山形県  鶴岡    39.9    1978-08-03
愛知県  名古屋  39.9    1942-08-02      愛知県  名古屋  39.9    1942-08-02

"""
