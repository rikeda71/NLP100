# -*- coding: utf-8 -*-
import re
from logistic import Logistic_Regression


def get_sentence_vector(sentence: str, features: list) -> list:
    """
    文章のベクトルを返す
    """

    value = len(features)
    sign = int(sentence[:2])
    vector = []

    # 単語分割
    words = re.split(r"[,.:;\s]", sentence[2:])
    while words.count("") > 0:
        words.remove("")

    # ベクトル作成
    for i in range(len(features)):
        if features[i][:-1] in words:
            vector.append(1.0)
        else:
            vector.append(0.0)

    # 文章の極性によってベクトルの位置を変更
    if sign == 1:
        return vector + [0] * value + [1.0]
    else:
        return [0] * value + vector + [1.0]


if __name__ == "__main__":
    features = []
    vectors = []
    sign = []
    with open("features.txt", "r") as f:
        for word in f.readlines():
            features.append(word)

    with open("sentiment.txt", "r") as f:
        for sentence in f.readlines():
            vectors.append(get_sentence_vector(sentence, features))
            if sentence[:2] == "+1":
                sign.append(1.0)
            else:
                sign.append(0.0)

    learn_circuit = Logistic_Regression(vectors, sign)
    learn_circuit.learn()
