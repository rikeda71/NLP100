from q96 import CountryVectors
import numpy as np
import random


def cos_sim(v1, v2) -> float:
    """
    numpy行列動詞のcos類似度を返す
    """

    try:
        return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    except:
        return 0.0


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
            repval = np.zeros(n)
            for name in cluster[i]:
                repval += vectors[name]
            repval /= len(cluster)
            reps[i] = repval
        # 各事例のクラスタへの割り当て
        for key, val in vectors.items():
            argmax_i = 0
            argmax_sim = cos_sim(reps[0], val)
            # もっとお類似度の高いクラスタを探す
            for i in range(1, k):
                sim = cos_sim(reps[i], v)
                if sim > argmax_sim:
                    argmax_i = i
                    argmax_sim = sim
            new_cluster[argmax_i].append(key)
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
        break


def main():
    cv = CountryVectors()
    k = 5
    k_means(cv.vectors, k)


if __name__ == "__main__":
    main()
