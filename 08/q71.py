# -*- coding:utf-8 -*-

""" 文章の中にストップワードが含まれるか判別 """


# stopwordの格納
stopwords = []
with open("stopword.txt", "r") as f:
    for line in f.readlines():
        stopwords.append(line.replace("\n", ""))


def include_stopword(sentence: str) -> bool:
    """
    引数に与えた文章に
    ストップワードが含まれるかどうかを返す
    """

    # 単語がstopwordに含まれるものか判別
    words = sentence.split(" ")
    for word in words:
        if word in stopwords:
            return True

    return False


if __name__ == "__main__":
    sentence = input()
    if include_stopword(sentence):
        print("include stopwords!")
    else:
        print("not include stopwords")
