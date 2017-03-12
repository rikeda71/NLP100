import re
# 文章
doc = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
# 辞書型
dict = {}
# 不要文字を削除
doc = re.sub(r'[.,]','',doc)
# 単語分解
word = re.split(r'[\s]',doc)
for i in range(len(word)) :
    # 参照位置の指定
    if i+1 in {1,5,6,7,8,9,15,16,19} :
        pos = 1
    else :
        pos = 2
    # 辞書への追加
    dict[word[i][:pos]] = i+1

print (dict)
