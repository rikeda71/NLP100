#coding:utf-8

col = [line.split('\t')[0] for line in open('hightemp.txt','r')]
new_col = list(set(col))
print('\n'.join(new_col))

"""
$ sdiff <(sort col/col1.txt | uniq) <(python 17.py | sort ) -w80
愛知県                                  愛知県
愛媛県                                  愛媛県
岐阜県                                  岐阜県
群馬県                                  群馬県
高知県                                  高知県
埼玉県                                  埼玉県
山形県                                  山形県
山梨県                                  山梨県
静岡県                                  静岡県
千葉県                                  千葉県
大阪府                                  大阪府
和歌山県                                和歌山県

"""
