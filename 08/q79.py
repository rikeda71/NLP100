from logistic import Logistic_Regression
from q73 import get_sentence_learn_vector
import matplotlib
import numpy as np


def main():
    vectors = []
    signs = []
    thresholds = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    precision = []
    recall = []

    # 素性のリストを用意
    with open("features.txt", "r") as f:
        features = [word[:-1] for word in f.readlines()]
    # 素性のリストを使って学習データを用意
    with open("sentiment.txt", "r") as f:
        for sentence in f.readlines():
            vector, sign = get_sentence_learn_vector(sentence, features)
            vectors.append(vector)
            signs.append(sign)

    # 正例，負例の数をカウント
    pos_count = 0
    neg_count = 0
    for sign in signs:
        if sign == 1.0:
            pos_count += 1
        else:
            neg_count += 1

    # 学習
    learn_circuit = Logistic_Regression(vectors, signs)
    # learn_circuit.learn()
    # 学習結果の格納
    with open("learndata.txt", "r") as f:
        learn_data = [float(val) for val in f.readlines()]
    learn_circuit.input_learn_data(learn_data)

    # 閾値を変更させながら精度を確認
    for value in thresholds:
        predicts = []
        # 予測
        for vector in vectors:
            if learn_circuit.get_prob(vector) >= value:
                predicts.append(1.0)
            else:
                predicts.append(-1.0)

        # カウント
        predict_pos_count = 0
        correct_count = 0
        correct_pos_count = 0
        for (sign, pred) in zip(signs, predicts):
            # 上から，予測した正例の数，
            # 予測が正解した数，予測が正例で正解した数のカウント
            if pred == 1.0:
                predict_pos_count += 1
            if sign == pred:
                correct_count += 1
                if sign == 1.0:
                    correct_pos_count += 1

        # 精度の計算
        precision_score = correct_pos_count / predict_pos_count
        recall_score = correct_pos_count / pos_count
        print("precision    \t" + str(precision_score))
        print("recall       \t" + str(recall_score))

        # 精度の格納
        precision.append(precision_score)
        recall.append(recall_score)

    # サーバー上で使用するときに必要
    matplotlib.use("Agg")
    # 描写
    import matplotlib.pyplot as plt
    plt.plot(np.array(precision), np.array(recall))
    plt.title("precision-recall graph")
    plt.xlabel("precision")
    plt.ylabel("recall")
    plt.savefig("graph.png")


if __name__ == "__main__":
    main()
