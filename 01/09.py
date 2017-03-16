import random

# 4文字以上の文字列の順番をランダムにする
def random_order(doc):
    word_list = doc.split(' ') # 単語ごとのリスト
    new_list = [] # 返却用のリスト
    for i in range(len(word_list)):
        # 4文字以下ならそのままの文字列を追加
        if len(word_list[i]) <= 4:
            new_list.append(word_list[i])
        # 5文字以上なら先頭末尾以外の文字列をシャッフル
        else:
            # 単語をとってきて、シャッフルするものだけ抽出
            word = word_list[i]
            shuffle_list = list(word_list[i][1:-1])
            # シャッフル!
            random.shuffle(shuffle_list)
            # リストに格納
            new_list.append(word[0]+"".join(shuffle_list)+word[-1])

    # 文章に整形しなおして返す
    return " ".join(new_list)

doc = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print("origin text:%s"%doc)
print("random text:%s"%random_order(doc))


"""
# random.shuffle()メソッドを使えば解決
# 先頭末尾以外の文字列をバラバラにして返す
def random_doc(doc):
    random_range = []
    # バラバラにする位置を格納
    for i in range(1, len(doc)-1):
        random_range.append(i)
    
    # バラバラにするリストの重複なし乱数の元
    index = random.sample(random_range, len(doc)-2)
    # 返す文字列を用意
    new_doc = doc[0]
    for i in range(len(index)):
        new_doc = new_doc + doc[index[i]]
    new_doc = new_doc + doc[-1]

    return new_doc
"""
