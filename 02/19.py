#coding:utf-8

col = [line.split('\t')[0] for line in open('hightemp.txt','r')]
dict = {}
# 文字列のカウント
for i in range(len(col)):
    if col[i] in dict:
        dict[col[i]] += 1
    else:
        dict[col[i]] = 1
sorted(dict.items(), key=lambda x:x[1], reverse=True)
print('\n'.join(k+ ' ' + str(v) for k, v in sorted(dict.items(), key=lambda x:x[1], reverse=True)))

"""
$ python 19.py
埼玉県 3
山形県 3
山梨県 3
群馬県 3
岐阜県 2
静岡県 2
愛知県 2
千葉県 2
高知県 1
和歌山県 1
愛媛県 1
大阪府 1

$ cut -f1 hightemp.txt | sort | uniq -c | sort -r
    3 山梨県
    3 山形県
    3 埼玉県
    3 群馬県
    2 千葉県
    2 静岡県
    2 岐阜県
    2 愛知県
    1 和歌山県
    1 大阪府
    1 高知県
    1 愛媛県

"""
