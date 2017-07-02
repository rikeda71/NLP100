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
    words = re.split(r"[,.:;\s]", sentence)
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


def Prediction(sentence: str="") -> str:
    """
    極性ラベルの予測をする
    +1 : 正例
    -1 : 負例
    """

    vector = get_sentence_vector(sentence, features)
    predict = learn_circuit.get_prob(vector)
    if predict >= 0.5:
        return "+1"
    else:
        return "-1"


# 素性の格納
features = []
with open("features.txt", "r") as f:
    for feature in f.readlines():
        features.append(feature)

# 学習結果の格納
learn_data = []
with open("learndata.txt", "r") as f:
    for val in f.readlines():
        learn_data.append(float(val))

learn_circuit = Logistic_Regression()
learn_circuit.input_learn_data(learn_data)


if __name__ == "__main__":
    sentence = input()
    print(Prediction(sentence))
