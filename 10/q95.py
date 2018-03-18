

def correlation_coefficient_of_spearman(data: list):
    """
    スピアマンの順位相関係数による評価
    """

    n = len(data)
    human = {}
    model = {}
    for line in data:
        split = line.split(",")
        key = split[0] + ":" + split[1]
        human[key] = float(split[2])
        model[key] = float(split[3])
    # 人が付けた順位を保存
    i = 0
    human_rank = {}
    for k, v in sorted(human.items(), key=lambda x: x[1], reverse=True):
        i += 1
        human_rank[k] = i

    # モデルが付けた順位を保存
    i = 0
    model_rank = {}
    for k, v in sorted(model.items(), key=lambda x: x[1], reverse=True):
        i += 1
        model_rank[k] = i

    # 人が付けた順位とモデルが付けた順位の差の2乗を求める
    di_2 = [(v - model_rank[k]) ** 2 for k, v in human_rank.items()]
    # 相関係数の導出
    rs = 1 - 6 * sum(di_2) / (n ** 3 - n)
    # t検定用のスコア
    # t = rs * ((n - 2) / (1 - (rs ** 2))) ** 0.5
    print("spearman : " + str(rs))


def main():
    with open("ppmi_wordsimilarity_353.csv", "r") as f:
        ppmi = [line.replace("\n", "") for line in f.readlines()]
    with open("w2v_wordsimilarity_353.csv", "r") as f:
        w2v = [line.replace("\n", "") for line in f.readlines()]

    print("ppmi ", end="")
    correlation_coefficient_of_spearman(ppmi)
    print("w2v  ", end="")
    correlation_coefficient_of_spearman(w2v)


if __name__ == "__main__":
    main()
