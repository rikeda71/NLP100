import re
# 文章
doc = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
# リスト
list = []
#不要文字を削除
doc = re.sub(r'[,.]','',doc)
# 文章から単語ごとに
word = re.split(r'[\s]+',doc)
for i in range(len(word)):
    list.insert(i,len(word[i]))

print(list)
