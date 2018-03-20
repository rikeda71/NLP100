from q96 import CountryVectors
import numpy as np
import random


def most_similer_index(repvec, vec, k: int) -> int:
    """
    各クラスタの代表ベクトルと距離を比較し、
    最も距離の近いクラスタ番号を返す
    """

    argmaxsim = float("inf")
    for i in range(k):
        sim = np.linalg.norm(repvec[i] - vec)
        if sim < argmaxsim:
            argmax_i = i
            argmaxsim = sim
    return argmax_i


def k_means(vectors: dict, k: int=2):
    """
    k-means法によるクラスタリングの結果を
    表示する関数
    """

    # クラスタを管理する辞書
    cluster = {}
    for i in range(k):
        cluster[i] = []
    # どのクラスタに入るかランダムで選定
    for key in vectors.keys():
        cluster[random.randint(0, k - 1)].append(key)

    # ベクトルの長さを取得
    for v in vectors.values():
        n = len(v)
        break

    flag = True
    # 収束するまで処理
    while flag:
        flag = False
        reps = {}
        new_cluster = {}
        # 代表値（ベクトル）の取得
        for i in range(k):
            new_cluster[i] = []
            reps[i] = sum([vectors[name] for name in cluster[i]]) / len(cluster[i])
        # 各事例のクラスタへの割り当て
        for key, val in vectors.items():
            new_cluster[most_similer_index(reps, val, k)].append(key)
        # 収束するかどうか
        for i in range(len(cluster)):
            if len(cluster[i]) != len(new_cluster[i]):
                cluster = new_cluster
                flag = True
                break
            else:
                elem = set(cluster[i])
                new_elem = set(new_cluster[i])
                if elem | new_elem != elem:
                    cluster = new_cluster
                    flag = True
                    break
    # 収束した
    for key, val in cluster.items():
        print(key, end="\t")
        print(val)


def main():
    cv = CountryVectors()
    k = 5
    k_means(cv.vectors, k)


if __name__ == "__main__":
    main()
