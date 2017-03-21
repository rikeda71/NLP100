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
doc1 = list('paraparaparadise')
doc2 = list('paragraph')
# doc1のbi-gram
X = n_gram(2,doc1)
X_set = set(X)
# doc2のbi-gram
Y = n_gram(2,doc2)
Y_set = set(Y)
# bi-gram集合の和集合,積集合,差集合
or_set = list(X_set | Y_set)
and_set = list(X_set & Y_set)
dif_set = list(X_set - Y_set)
print('OR :%s\nAND:%s\nDIF:%s' %(or_set, and_set, dif_set) )
print('\n\'se\'が存在するか\nX:%s\nY:%s'%('se' in X_set, 'se' in Y_set))
