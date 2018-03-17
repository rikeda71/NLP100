from scipy import io
import numpy as np


def cos_sim_val(v1, v2) -> float:
    """
    cos類似度の導出
    """

    np_v1 = np.array(v1)
    np_v2 = np.array(v2)
    ab = np.dot(np_v1, np_v2)
    a = np.linalg.norm(np_v1)
    b = np.linalg.norm(np_v2)
    sim_val = ab / a / b
    if sim_val != sim_val:
        return 0
    return sim_val


def main():
    # 次元圧縮したベクトルを取得
    with open("matrix_x.txt", "r") as f:
        words = [word[:-1] for word in f.readlines()]
    vectors = io.loadmat("matrix_300.mat")["a"]

    target_vec = vectors[index]
    index = words.index("England")
    vec_dict = {}
    # Englandとそれ以外の類似度を格納
    for i in range(len(vectors)):
        if words[i] == "England":
            continue
        vec_dict[words[i]] = cos_sim_val(target_vec, vectors[i])

    # Englandと類似度の高い上位10単語を出力
    sorted_vec = sorted(vec_dict.items(), key=lambda x: x[1], reverse=True)
    for i in range(10):
        print(sorted_vec[i][0], end="\t")
        print(sorted_vec[i][1])


if __name__ == "__main__":
    main()
