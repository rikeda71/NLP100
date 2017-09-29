# -*- coding: utf-8 -*-
from math import log


def PPMI(N: float, f_t_c: float, f_t_a: float, f_a_c: float) -> float:
    """
    return Positive Pointwise Mutual Information
    """
    return max(log(N * f_t_c / f_t_a / f_a_c), 0)


def get_word_count_dict(path: str) -> dict:
    """
    テキストデータから語と出現回数の対を保持した
    辞書を取得する
    """
    dic = {}
    with open(path, "r") as f:
        line = f.readline()
        while line:
            split = line.split(" ")
            dic[split[0]] = int(split[1])
            line = f.readline()
    return dic


def main():
    cooc_dic = {}
    matrix = {}
    # 値を保持する共起だけ抽出
    with open("count/cooc.txt", "r") as f:
        line = f.readline()
        while line:
            split = line.split(" ")
            # f(t,c) >= 10のとき
            if int(split[1]) >= 10:
                cooc_dic[split[0]] = int(split[1])
            line = f.readline()

    word_dic = get_word_count_dict("count/word.txt")
    cont_dic = get_word_count_dict("count/cont.txt")
    with open("count/N.txt", "r") as f:
        N = int(f.readline())

    # PPMIの計算
    for k, v in cooc_dic.items():
        split = k.split("\t")
        matrix[k] = PPMI(N, v, word_dic[split[0]], cont_dic[split[1]])

    # 書き込み
    text = ""
    for k, v in matrix.items():
        text += k + " " + str(v) + "\n"
    with open("matrix.txt", "w") as f:
        f.write(text)


if __name__ == "__main__":
    main()
