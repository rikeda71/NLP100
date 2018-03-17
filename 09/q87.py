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
    return ab / a / b


def main():
    # 次元圧縮したベクトルを取得
    with open("matrix_x.txt", "r") as f:
        words = [word[:-1] for word in f.readlines()]
    vectors = io.loadmat("matrix_300.mat")["a"]
    # United States と U.Sの類似度を表示
    index1 = words.index("United_States")
    index2 = words.index("U.S")
    a = vectors[index1]
    b = vectors[index2]
    print(cos_sim_val(a, b))


if __name__ == "__main__":
    main()
