# -*- coding: utf-8 -*-
import re
from logistic import Logistic_Regression
from nltk import PorterStemmer
from q73 import get_sentence_vector
from q74 import Prediction


def main():
    # 素性の格納
    with open("features.txt", "r") as f:
        features = [feature[:-1] for feature in f.readlines()]

    # 学習結果の格納
    with open("learndata.txt", "r") as f:
        learn_data = [float(val) for val in f.readlines()]

    # 学習
    learn_circuit = Logistic_Regression()
    learn_circuit.input_learn_data(learn_data)

    # ラベル付け
    with open("sentiment.txt", "r") as f:
        for sentence in f.readlines():
            print(sentence[:2], end="\t")
            predict_prob = Prediction(sentence)
            if predict_prob >= 0.5:
                label = "+1"
            else:
                label = "-1"
            print(label + "\t", str(predict_prob))


if __name__ == "__main__":
    main()
