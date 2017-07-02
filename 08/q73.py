# -*- coding: utf-8 -*-
import re
from logistic import Logistic_Regression
from nltk import PorterStemmer


def get_sentence_vector(sentence: str, features: list) -> list:
    """
    文章のベクトルを返す
    """

    vector = []
    stemmer = PorterStemmer()
    stem_words = []

    # 単語分割
    words = re.split(r"[,.:;\s]", sentence[2:])
    while words.count("") > 0:
        words.remove("")
    for word in words:
        stem_words.append(stemmer.stem(word))

    # ベクトル作成
    for i in range(len(features)):
        if features[i][:-1] in stem_words:
            vector.append(1.0)
        else:
            vector.append(0.0)

    return vector


def get_sentence_learn_vector(sentence: str, features: list) -> list:
    """
    学習のための文章のベクトルを返す
    """
    sign = int(sentence[:2])
    value = len(features)
    vector = get_sentence_vector(sentence, features)

    # 文章の極性によってベクトルの位置を変更
    if sign == 1:
        # return vector + [0] * value + [1.0]
        return vector + [0] * value
    else:
        # return [0] * value + vector + [1.0]
        return [0] * value + vector


if __name__ == "__main__":
    features = []
    vectors = []
    sign = []
    with open("features.txt", "r") as f:
        for word in f.readlines():
            features.append(word)

    with open("sentiment.txt", "r") as f:
        for sentence in f.readlines():
            vectors.append(get_sentence_learn_vector(sentence, features))
            if sentence[:2] == "+1":
                sign.append(1.0)
            else:
                sign.append(0.0)

    learn_circuit = Logistic_Regression(vectors, sign)
    learn_circuit.learn()
    with open("learndata.txt", "w") as f:
        data = map(str, learn_circuit.get_learn_data())
        f.write("\n".join(data))
    with open("sentiment.txt", "r") as f:
        vec = get_sentence_vector(f.readlines()[23], features)
        print(learn_circuit.get_pos_prob(vec))
        print(learn_circuit.get_neg_prob(vec))
