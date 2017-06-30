# -*- coding:utf-8 -*-
from q71 import include_stopword
import re
from nltk import PorterStemmer
from collections import Counter


def get_features(sentences: list) -> list:
    """
    学習データから素性を抽出する
    引数の構造:
    sentences=[sentence, sentence, ... , sentence]
    正例と負例に分けて辞書型に格納
    辞書の値はそれぞれ正例、負例の文
    """

    features = []
    features_candidate = []
    stemmer = PorterStemmer()

    # stopword以外を格納
    for sentence in sentences:
        words = re.split(r"[,.:;\s]", sentence)
        while words.count("") > 0:
            words.remove("")
        for word in words:
            word = stemmer.stem(word)
            if include_stopword(word):
                pass
            else:
                features_candidate.append(word)

    # 出現回数が5回以下のものをすべて削除
    # それ以外を素性として返す
    counter = Counter(features_candidate)
    for word, cnt in counter.most_common():
        if cnt < 10:
            break
        else:
            if len(word) > 1:
                features.append(word)

    return features


def get_features_of_file(filename: str):
    """
    ファイルを読み込み素性を返す
    """
    sentences = []
    with open(filename, "r") as f:
        for sentence in f.readlines():
            sentences.append(sentence[2:])
    return get_features(sentences)


if __name__ == "__main__":
    features = get_features_of_file("sentiment.txt")
    print("\n".join(features))
