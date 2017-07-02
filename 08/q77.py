# -*- coding: utf-8 -*-


def f_measure(precision: float="", recall: float=""):
    """
    f値を返す
    """
    return (2 * precision * recall) / (precision + recall)


def main():
    # 正例，負例の回数のカウント
    pos_count = 0
    neg_count = 0
    with open("sentiment.txt", "r") as f:
        for sentence in f.readlines():
            if sentence[:2] == "+1":
                pos_count += 1
            else:
                neg_count += 1

    # 正解の回数のカウント
    correct_count = 0
    correct_pos_count = 0
    predict_pos_count = 0
    with open("ans76.txt", "r") as f:
        for result in f.readlines():
            split_result = result.split("\t")
            if split_result[1] == "+1":
                predict_pos_count += 1
            # ラベルが同じなら
            if split_result[0] == split_result[1]:
                correct_count += 1
                # 更にラベルが正例なら
                if split_result[0] == "+1":
                    correct_pos_count += 1

    # 結果の出力
    precision = correct_pos_count / predict_pos_count
    recall = correct_pos_count / pos_count
    print("accuracy rate\t" + str(correct_count / (pos_count + neg_count)))
    print("precision\t" + str(precision))
    print("recall   \t" + str(recall))
    print("f1       \t" + str(f_measure(precision, recall)))


if __name__ == "__main__":
    main()
