#coding:utf-8
import re

# 与えられた文字列リストからn-gramを返す
def n_gram(n,doc):
    list = []
    for i in range(len(doc)):
        if i+n-1 < len(doc):
            list.insert(i,"".join(doc[i:i+n]))
    return list

# 文章
doc = 'I am an NLPer'
# 1文字ずつ分解
str_doc = list(re.sub('[\W]','',doc))
# 1単語ずつ分解
cha_doc = doc.split(' ')

# 単語bi-gram
str_bigram = n_gram(2,str_doc)
# 文字bi-gram
cha_bigram = n_gram(2,cha_doc)

print('文字bi-gram\n %s'%str_bigram)
print('単語bi-gram\n %s'%cha_bigram)
