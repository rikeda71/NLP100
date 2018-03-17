from scipy import sparse, io
import numpy as np
import sklearn.decomposition


"""
主成分分析(principal component analysis)を使いたかったが，
pcaのライブラリと共分散行列を導出するメソッドが疎行列に対応してないため
特異値分解による次元削減としている
"""


def svd(np_array):
    """
    特異値分解(singular value deconposition)を行い
    得られた3つの行列を返す
    http://ohke.hateblo.jp/entry/2017/12/14/230500参考
    sklearnやnumpyにもsvdは実装されているので使わなくてok
    """

    # c^TCの固有値，固有ベクトルの計算
    ct_c = np.dot(np_array.T, np_array)
    eigenvalue, eigenvector = np.linalg.eig(ct_c)

    # 特異値の計算
    sing_value = np.sqrt(eigenvalue)
    sing_index = np.argsort(singular_value)[::-1]

    # 特異値行列の計算
    sigma = np.diag(sing_value[sing_index])

    # 右特異行列の計算
    v = eigenvector[:, sing_index]

    # 左特異行列の計算
    u = np.array([np.dot(c, v[:, i]) / sigma.diagonal()[i]
                  for i in range(len(sigma.diagonal()))]).T

    return u, sigma, v


def main():
    matrix = io.loadmat("matrix_t_to_c.mat")["a"]
    # 分散共分散行列の導出(https://mathtrain.jp/varcovmatrix)
    # 共分散の導出(https://mathtrain.jp/covariance)
    # 共分散が大きい(正) -> Xが大きいときYも大きい傾向がある
    # 共分散が0に近い    -> XとYにあまり関係はない
    # 共分散が小さい(負) -> Xが大きいときYが小さい傾向がある
    svd = sklearn.decomposition.TruncatedSVD(300)
    matrix_300 = svd.fit_transform(matrix)
    io.savemat("matrix_300", {"a": matrix_300})


if __name__ == "__main__":
    main()
