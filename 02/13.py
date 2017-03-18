#config:utf-8

# 文字列を格納するリストを用意
str1 = []
str2 = []
new_str = ''

# 各テキストから文字列を得る
for line in open('col/col1.txt','r'):
    str1.append(line.strip('\n'))

for line in open('col/col2.txt','r'):
    str2.append(line.strip('\n'))

# 結合
length = len(str1)-1
for i in range(length):
    new_str = new_str + str1[i] + '\t' + str2[i] + '\n'
new_str = new_str + str1[length] + '\t' + str2[length]

# テキストファイルの作成
print(new_str)
f = open('col/paste.txt','w')
f.write(new_str)
f.close()

"""
$ sdiff --width=80 <(paste col/col1.txt col/col2.txt) <(python 13.py)
高知県  江川崎                          高知県  江川崎
埼玉県  熊谷                            埼玉県  熊谷
岐阜県  多治見                          岐阜県  多治見
山形県  山形                            山形県  山形
山梨県  甲府                            山梨県  甲府
和歌山県        かつらぎ                和歌山県        かつらぎ
静岡県  天竜                            静岡県  天竜
山梨県  勝沼                            山梨県  勝沼
埼玉県  越谷                            埼玉県  越谷
群馬県  館林                            群馬県  館林
群馬県  上里見                          群馬県  上里見
愛知県  愛西                            愛知県  愛西
千葉県  牛久                            千葉県  牛久
静岡県  佐久間                          静岡県  佐久間
愛媛県  宇和島                          愛媛県  宇和島
山形県  酒田                            山形県  酒田
岐阜県  美濃                            岐阜県  美濃
群馬県  前橋                            群馬県  前橋
千葉県  茂原                            千葉県  茂原
埼玉県  鳩山                            埼玉県  鳩山
大阪府  豊中                            大阪府  豊中
山梨県  大月                            山梨県  大月
山形県  鶴岡                            山形県  鶴岡
愛知県  名古屋                          愛知県  名古屋

"""
