from sklearn.model_selection import KFold
from logistic import Logistic_Regression
from q73 import get_sentence_learn_vector
from q77 import f_measure


def main():
    vectors = []
    signs = []
    K = 5
    k_fold = KFold(n_splits=K, shuffle=True)

    # 素性のリストを用意
    with open("features.txt", "r") as f:
        features = [word[:-1] for word in f.readlines()]
    # 素性のリストを使って学習データを用意
    with open("sentiment.txt", "r") as f:
        for sentence in f.readlines():
            vector, sign = get_sentence_learn_vector(sentence, features)
            vectors.append(vector)
            signs.append(sign)

    accuracy_rate = []
    precision = []
    recall = []
    f1 = []
    # 交差検定
    for train, test in k_fold.split(vectors):
        X_train = [vectors[i] for i in train]
        y_train = [signs[i] for i in train]
        X_test = [vectors[i] for i in test]
        y_test = [signs[i] for i in test]
        y_pred = []

        # 学習
        learn_circuit = Logistic_Regression(X_train, y_train)
        learn_circuit.learn()
        # 予測
        for vector in X_test:
            if learn_circuit.get_prob(vector) >= 0.5:
                y_pred.append(1.0)
            else:
                y_pred.append(-1.0)

        # カウント
        pos_count = 0
        neg_count = 0
        predict_pos_count = 0
        correct_count = 0
        correct_pos_count = 0
        for (sign, pred) in zip(y_test, y_pred):
            # 上から，正例の数，負例の数，予測した正例の数，
            # 予測が正解した数，予測が正例で正解した数のカウント
            if sign == 1.0:
                pos_count += 1
            else:
                neg_count += 1
            if pred == 1.0:
                predict_pos_count += 1
            if sign == pred:
                correct_count += 1
                if sign == 1.0:
                    correct_pos_count += 1

        # 精度の計算
        accuracy_rate_score = correct_count / (pos_count + neg_count)
        precision_score = correct_pos_count / predict_pos_count
        recall_score = correct_pos_count / pos_count
        f1_score = f_measure(precision_score, recall_score)
        print("accuracy_rate\t" + str(accuracy_rate_score))
        print("precision    \t" + str(precision_score))
        print("recall       \t" + str(recall_score))
        print("f1           \t" + str(f1_score), end="\n\n")

        # 精度の格納
        accuracy_rate.append(accuracy_rate_score)
        precision.append(precision_score)
        recall.append(recall_score)
        f1.append(f1_score)

    # 精度の確認
    print("5分割交差検定の結果")
    print("accuracy_rate\t" + str(sum(accuracy_rate) / K))
    print("precision    \t" + str(sum(precision) / K))
    print("recall       \t" + str(sum(recall) / K))
    print("f1           \t" + str(sum(f1) / K))


if __name__ == "__main__":
    main()
