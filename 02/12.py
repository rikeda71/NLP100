#coding:utf-8

str1 = '' # col1.txtのテキスト
str2 = '' # col2.txtのテキスト
for line in open('hightemp.txt','r'):
    # 1行をtab文字ごとに分割し1列目,2列目を保持
    text = line.split("\t")
    str1 = str1 + text[0] + '\n'
    str2 = str2 + text[1] + '\n'
    print(text[0],text[1])

# write col1.txt
f = open('col/col1.txt','w')
f.write(str1)
f.close()
# write col2.txt
f = open('col/col2.txt','w')
f.write(str2)
f.close()

"""
$ sdiff <(cut -f1,2 hightemp.txt) <(python 12.py) --width=80
高知県  江川崎                        | 高知県 江川崎
埼玉県  熊谷                          | 埼玉県 熊谷
岐阜県  多治見                        | 岐阜県 多治見
山形県  山形                          | 山形県 山形
山梨県  甲府                          | 山梨県 甲府
和歌山県        かつらぎ              | 和歌山県 かつらぎ
静岡県  天竜                          | 静岡県 天竜
山梨県  勝沼                          | 山梨県 勝沼
埼玉県  越谷                          | 埼玉県 越谷
群馬県  館林                          | 群馬県 館林
群馬県  上里見                        | 群馬県 上里見
愛知県  愛西                          | 愛知県 愛西
千葉県  牛久                          | 千葉県 牛久
静岡県  佐久間                        | 静岡県 佐久間
愛媛県  宇和島                        | 愛媛県 宇和島
山形県  酒田                          | 山形県 酒田
岐阜県  美濃                          | 岐阜県 美濃
群馬県  前橋                          | 群馬県 前橋
千葉県  茂原                          | 千葉県 茂原
埼玉県  鳩山                          | 埼玉県 鳩山
大阪府  豊中                          | 大阪府 豊中
山梨県  大月                          | 山梨県 大月
山形県  鶴岡                          | 山形県 鶴岡
愛知県  名古屋                        | 愛知県 名古屋
"""
