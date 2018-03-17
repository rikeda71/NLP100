# -*- coding: utf-8 -*-
from math import log
from scipy import io, sparse


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

    # t:単語, c:文脈語
    t = []
    c = []
    for k in cooc_dic.keys():
        split = k.split("\t")
        t.append(split[0])
        c.append(split[1])
    t = sorted(list(set(t)))
    c = sorted(list(set(c)))

    """
    # 疎行列の用意
    a = sparse.lil_matrix((len(t), len(c)))
    # PPMIの計算
    for k, v in cooc_dic.items():
        s = k.split("\t")
        i = t.index(s[0]) if s[0] in t else -1
        j = c.index(s[1]) if s[1] in c else -1
        if i < 0 or j < 0:
            continue
        a[i, j] = PPMI(N, v, word_dic[s[0]], cont_dic[s[1]])
    """

    # 書き込み
    # io.savemat("matrix_t_to_c", {"a": a})
    with open("matrix_x.txt", "w") as f:
        f.write("\n".join(t))
    with open("matrix_y.txt", "w") as f:
        f.write("\n".join(c))


if __name__ == "__main__":
    main()
