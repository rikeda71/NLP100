# -*- coding: utf-8 -*-


def main():
    # 素性の格納
    features = []
    with open("features.txt", "r") as f:
        for feature in f.readlines():
            features.append(feature[:-1])

    # 学習データの格納
    learn_data = []
    with open("learndata.txt", "r") as f:
        for val in f.readlines():
            learn_data.append(float(val))

    # 素性と学習結果の紐づけ
    feature_dict = {}
    for i in range(len(learn_data)):
        feature_dict[features[i]] = learn_data[i]

    # ソート
    sort_dict = sorted(feature_dict.items(), key=lambda x: x[1])

    # 重みの高い素性Top10
    dict_length = len(sort_dict)
    for i in range(dict_length - 1, dict_length - 11, -1):
        dic = sort_dict[i]
        print(str(dic[0]) + "\t" + str(dic[1]))

    # 重みの低い素性Top10
    for i in range(10):
        dic = sort_dict[i]
        print(str(dic[0]) + "\t" + str(dic[1]))


if __name__ == "__main__":
    main()
